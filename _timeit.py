import time


def timeit(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f'duration time: {end - start}')

    return inner
