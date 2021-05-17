### overview

Este ejercicio está pensado para empezar a romper mano con programación asíncrona en python 3 moderno.

* cada uno intenta resolver el ejercicio de forma independiente
* justo antes de la reunión para presentar ejercicios subimos nuestras soluciones a nuestros forks de este repo para que sea fácil compartirlas con los demás

Para este ejercicio, revisar:

* qué es un [event loop](https://en.wikipedia.org/wiki/Event_loop) ?
* qué es un [future](https://en.wikipedia.org/wiki/Futures_and_promises) ?
* qué es un `Awaitable` en python ?
* recomiendo leer esto: https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

![dali_clocks](dali_clocks.png)

### ejercicio

Este código, que ha programado un consultor experto en ingeniería industrial por 100,000 euros, simula en tiempo real una fábrica de botas. El número de botas construidas hasta el momento se encuentra en la variable global `BOOTS`.

```python
import asyncio
import random

BOOTS = 0

async def make_boot():
    global BOOTS
    manufacturing_time = random.choice([1,3,5])
    await asyncio.sleep(manufacturing_time)
    BOOTS += 1

async def worker():
    while 1:
        await make_boot()

async def main():
    await worker()

asyncio.run(main())
```

Por desgracia, faltan cosas y hay nuevos requisitos y el consultor se ha ido al caribe.

#### pregunta 1

Respuesta en un archivo `boot_factory_1.py`

Ahora mismo el programa funciona, pero el consultor se ha olvidado de emitir a pantalla el número de botas construidas.

Modifica el programa para que, *aproximadamente* una vez por segundo, haga print del tiempo transcurrido desde el principio de la simulación y del número de botas construidas hasta ese momento, eg.

```
seconds: 0.00 boots: 0
seconds: 1.00 boots: 0
seconds: 2.00 boots: 0
seconds: 3.01 boots: 0
seconds: 4.01 boots: 0
seconds: 5.02 boots: 1
seconds: 6.02 boots: 2
seconds: 7.02 boots: 2
...
```

#### pregunta 2

Respuesta en un archivo `boot_factory_2.py`

Ahora la simulación está hardcodeada a 1 solo worker.

Modifica el código para que se le pueda pasar el número de workers concurrentes trabajando en la fábrica por línea de comandos, ej.

`python3 boot_factory_2.py 3`

#### pregunta 3

Respuesta en un archivo `boot_factory_3.py`

Según cómo se haya implementado la funcionalidad de printear info 1 vez por segundo en la pregunta 1, es posible que haya [clock drift](https://en.wikipedia.org/wiki/Clock_drift): es decir, que los prints no coincidan exactamente con los segundos transcurridos desde el principio de la simulación.

¿Puedes modificar el código para corregir el drift? Deberíamos ver algo como:

```
seconds: 0.00 boots: 0
seconds: 1.00 boots: 0
seconds: 2.00 boots: 0
seconds: 3.00 boots: 0
seconds: 4.00 boots: 0
seconds: 5.00 boots: 1
seconds: 6.00 boots: 2
seconds: 7.00 boots: 2
...
```
