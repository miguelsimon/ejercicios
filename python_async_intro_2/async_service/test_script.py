import requests
import concurrent.futures


def squared(url, num):
    response = requests.get(url, params={"num": num})
    return float(response.text)


if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)

    xs = [0, 1, 2, 3]
    futures = [
        executor.submit(squared, "http://localhost:8888/calculate_square", x)
        for x in xs
    ]
    ys = [future.result() for future in futures]

    print(ys)
