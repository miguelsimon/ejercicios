import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest

SPECS = dict(
    CYLINDER_RADIUS_METRES = 2.0,
    MIN_LEVEL_METRES = 0.0,
    MAX_LEVEL_METRES = 7.0,
    IN_PIPE_RADIUS_METRES = 20 / 100.0,
    OUT_PIPE_RADIUS_METRES = 100 / 100.0,
    IN_MAX_FLOW_RATE_M3_S = 5.0,
    DEMAND_BASELINE_RATE_M3_S = 0.5,
    OUT_MAX_FLOW_RATE_M3_S = 80.0,
)

def m3_to_level(m3):
    section = np.pi * SPECS['CYLINDER_RADIUS_METRES'] ** 2
    return m3 / section

def level_to_m3(level):
    section = np.pi * SPECS['CYLINDER_RADIUS_METRES'] ** 2
    return level * section

class State:
    def __init__(self, m3_0, demand_0):

        self.t = [0.0]
        self.m3 = [m3_0]
        self.demand = [demand_0]

        self.setpoint = []
        self.controller_output = []
        self.delta_demand = []
        self.in_signal = []
        self.in_flow = []
        self.out_flow = []

    def get_time(self):
        return self.t[-1]

    def get_process_var(self):
        return m3_to_level(self.m3[-1])

    def step(self, dt, setpoint, controller_output, delta_demand):
        self.setpoint.append(setpoint)
        self.controller_output.append(controller_output)
        self.delta_demand.append(delta_demand)

        in_signal = np.clip(controller_output, 0.0, 1.0)
        self.in_signal.append(in_signal)

        demand = self.demand[-1]
        m3 = self.m3[-1]
        m3_max = level_to_m3(SPECS['MAX_LEVEL_METRES'])

        in_flow = in_signal * SPECS['IN_MAX_FLOW_RATE_M3_S'] * dt
        out_flow = min(SPECS['OUT_MAX_FLOW_RATE_M3_S'] * dt, demand)

        net_flow = in_flow - out_flow

        # balance mass
        if m3 + net_flow < 0:
            out_flow = in_flow + m3
        elif m3 + net_flow > m3_max:
            in_flow = m3_max - m3 + out_flow

        self.in_flow.append(in_flow)
        self.out_flow.append(out_flow)

        self.t.append(self.t[-1] + dt)
        self.m3.append(self.m3[-1] + self.in_flow[-1] - self.out_flow[-1])
        self.demand.append(self.demand[-1] + self.delta_demand[-1] - self.out_flow[-1])

    def get_dataframe(self):
        d = {
            "time": self.t,
            "m3": self.m3,
            "demand": self.demand,

            "setpoint": [0.0] + self.setpoint,
            "controller_output": [0.0] + self.controller_output,
            "delta_demand": [0.0] + self.delta_demand,
            "in_signal": [0.0] + self.in_signal,
            "in_flow": [0.0] + self.in_flow,
            "out_flow": [0.0] + self.out_flow,
        }

        df = pd.DataFrame(d)
        df['level'] = m3_to_level(df['m3'])
        return df


class Sim:
    def __init__(self, dt, state, controller, environment):
        process_var = state.get_process_var()
        controller.initialize_controller(process_var, dt)

        self.dt = dt
        self.state = state
        self.controller = controller
        self.environment = environment

    def step(self):
        t = self.state.get_time()
        dt = self.dt

        process_var = self.state.get_process_var()

        setpoint = self.environment.get_setpoint()
        delta_demand = self.environment.get_delta_demand()

        self.controller.change_setpoint(setpoint)
        controller_output = self.controller.get_output(process_var)

        self.state.step(dt, setpoint, controller_output, delta_demand)
        self.environment.step(dt)

    def run(self, t):
        while self.state.get_time() < t:
            self.step()


class Controller:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.dt = None
        self.setpoint = None
        self.integrated_error = None
        self.last_error = None

    def initialize_controller(self, v, dt):
        self.dt = dt
        self.integrated_error = 0
        self.last_error = 0

    def change_setpoint(self, setpoint):
        self.setpoint = setpoint

    def get_output(self, v):
        dt = self.dt

        error = self.setpoint - v
        derror_dt = (error - self.last_error) / dt
        self.integrated_error += error * dt
        self.last_error = error

        return error * self.kp + self.ki * self.integrated_error + self.kd * derror_dt


class Environment:
    def __init__(self, initial_setpoint, initial_delta_demand, events):
        self.events = events
        self.event_queue = sorted(events, key=lambda d: -d['time'])

        self.t = [0]
        self.setpoint = [initial_setpoint]
        self.delta_demand = [initial_delta_demand]

    def get_setpoint(self):
        return self.setpoint[-1]

    def get_delta_demand(self):
        return self.delta_demand[-1]

    def step(self, dt):
        self.t.append(self.t[-1] + dt)
        self.delta_demand.append(dt * SPECS['DEMAND_BASELINE_RATE_M3_S'])
        self.setpoint.append(self.setpoint[-1])

        while self.is_event_pending():
            self.pop_handle_event()

    def get_events(self):
        return self.events

    def is_event_pending(self):
        if len(self.event_queue) > 0:
            next_event_at = self.event_queue[-1]["time"]
            return next_event_at <= self.t[-1]

    def pop_handle_event(self):
        event = self.event_queue.pop()
        if event["type"] == "change_setpoint":
            self.setpoint[-1] = event["setpoint"]
        elif event["type"] == "add_demand":
            self.delta_demand[-1] += event["m3"]
        else:
            raise Exception("unknown event")


def simulate_normal(controller):
    """
    Normal operation smoothing demand peaks
    """

    events = [
        {"time": 1, "type": "add_demand", "m3": 2.0},
        {"time": 5, "type": "add_demand", "m3": 9.0},
        {"time": 8, "type": "add_demand", "m3": 4.0},
    ]
    environment = Environment(initial_setpoint = 5.0, initial_delta_demand=0.0, events=events)

    dt = 0.01
    state = State(m3_0 = level_to_m3(5.0), demand_0 = 0.0)
    sim = Sim(
        dt=dt,
        state=state,
        controller=controller,
        environment=environment,
    )
    sim.run(10)
    return sim.state.get_dataframe(), sim.environment.get_events()

def simulate_strange(controller):
    """
    demonstrate integral windup
    """

    events = [
        #{"time": 2, "type": "change_setpoint", "setpoint": 2.0},
    ]
    environment = Environment(initial_setpoint = 5.0, initial_delta_demand=0.0, events=events)

    dt = 0.01
    state = State(m3_0 = level_to_m3(0.0), demand_0 = 0.0)
    sim = Sim(
        dt=dt,
        state=state,
        controller=controller,
        environment=environment,
    )
    sim.run(100)
    return sim.state.get_dataframe(), sim.environment.get_events()


def plot_simulation(df, events):
    f, ax = plt.subplots(1)
    ax2 = ax.twinx()

    ax.set_ylabel("level", color="g")
    ax.set_ylim((SPECS['MIN_LEVEL_METRES'] -1, SPECS['MAX_LEVEL_METRES'] + 1))
    ax.set_xlabel("seconds")
    ax.plot(df["time"], df["level"], "g")
    ax.plot(df["time"], df["setpoint"], "r--")

    ax2.set_ylim((-0.1, 1.1))
    ax2.set_ylabel("in_signal", color="b")
    ax2.plot(df["time"], df["in_signal"], "b")

    for event in events:
        ax.axvline(event["time"], color="black")
        ax.text(event["time"], 0, event["type"], rotation=270)

    return f, ax


class Test(unittest.TestCase):
    def test_simulate_normal(self):
        controller = Controller(1.0, 0.0, 0.0)
        simulate_normal(controller)

    def test_simulate_strange(self):
        controller = Controller(1.0, 0.0, 0.0)
        simulate_strange(controller)
