from datetime import datetime
from functools import wraps
from time import perf_counter


def get_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = perf_counter()
        func(*args, **kwargs)
        e = perf_counter()
        print(f"Time: {e - s} seconds")

    return wrapper


def timestamp() -> str:
    return f"{datetime.now():%H:%M:%S}"


def kill_time():
    for _ in range(10**9):
        pass
