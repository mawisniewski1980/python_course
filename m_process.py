import functools
import multiprocessing as mp
import os
import time
from multiprocessing import Pipe, Process, current_process, Queue, Lock, Semaphore
from random import randint

from course.time_stuff import timestamp, kill_time, get_time


def func(param):
    print(f"Starting: {mp.current_process().name} ({os.getpid()})... ({timestamp()})")
    kill_time()
    print(f"{os.getpid()} finished! ({timestamp()})")


@get_time
def main_processes():
    print(" PROCESSES")

    process = mp.Process(name="Process-1", target=func, args=("Sample",))
    process2 = mp.Process(name="Process-2", target=func, args=("Sample2",))

    process.start()
    process2.start()

    process.join()
    process2.join()


def convert_t_x(number: int) -> str:
    time.sleep(2)
    # kill_time()
    return number * "x"


@get_time
def main_pools_map(cores: int = 7):
    print(" POOLS MAP")
    print(f"Cores Available: {mp.cpu_count()}")

    values: tuple[int, ...] = tuple(range(1, cores))

    # with mp.Pool(processes=3) as pool:   with limiter = only 3 processors
    with mp.Pool() as pool:
        results: list[str] = pool.map(convert_t_x, values)
        print("Results", results)


def add_numbers(*args) -> float:
    time.sleep(2)
    return sum(args)


@get_time
def main_pools_starmap():
    print(" POOLS STARMAP")
    print(f"Cores Available: {mp.cpu_count()}")

    values = ((1, 2, 10), (3, 4), (5, 6, 111, 111))

    with mp.Pool() as pool:
        results: list[float] = pool.starmap(add_numbers, values)
        print("Results", results)


def func_a(param):
    time.sleep(2)
    return param


def func_b(param):
    time.sleep(2)
    return param


def func_c(param, param2):
    time.sleep(2)
    return param, param2


def map_func(func):
    return func()


@get_time
def main_pools_multi_func():
    print(" POOLS MULTI FUNC")
    print(f"Cores Available: {mp.cpu_count()}")

    a = functools.partial(func_a, "A")
    b = functools.partial(func_b, "B")
    c = functools.partial(func_c, "C", "C2")

    with mp.Pool() as pool:
        results = pool.map(map_func, [a, b, c])
        print("Results", results)


numbers: list[int] = [0]


def func():
    global numbers

    numbers.extend([1, 2, 3])
    print(f"Process data: {numbers}")


def main_data_sharing_issue():
    print(" POOLS DATA SHARING ISSUE")  # process do not share memory
    print(f"Cores Available: {mp.cpu_count()}")
    process = mp.Process(target=func)
    process.start()
    process.join()

    print("Main data: ", numbers)


def main_pipes():
    print(" PIPES")
    print(f"Cores Available: {mp.cpu_count()}")

    c1, c2 = Pipe()

    c2.send("Hello!")
    print("Data to be received:", c1.poll())

    if c1.poll():
        obj = c1.recv()
        print(obj)
    print("Data to be received:", c1.poll())


def sender(connection):
    print(f"Sender: {current_process().name} ({os.getpid()})...")

    for _ in range(5):
        rand: int = randint(1, 10)
        connection.send(rand)
        print(f"{rand} was sent...")
        time.sleep(0.5)

    print('Sending: "None"...')
    connection.send(None)
    print("Done with sending data!")


def receiver(connection):
    print(f"Reciever: {current_process().name} ({os.getpid()})...")

    while True:
        data = connection.recv()
        print(f"{data} was received")

        if data is None:
            break

    print("Done with receiving data!")


def main_pipes2():
    print(" PIPES")
    print(f"Cores Available: {mp.cpu_count()}")

    c1, c2 = Pipe()

    s = Process(target=sender, args=(c2,))
    r = Process(target=receiver, args=(c1,))

    s.start()
    r.start()

    s.join()
    r.join()


def insert_val(queue: Queue, i: int):
    print(f"{i} was put in the queue...")
    queue.put(i)


def main_queues():
    print(" QUEUES 1")
    print(f"Cores Available: {mp.cpu_count()}")

    queue: Queue = Queue()
    processes = [Process(target=insert_val, args=(queue, i)) for i in range(5)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    results = [queue.get() for _ in processes]
    print(f"Results: {results}")


def func(queue: Queue):
    name = current_process().name

    try:
        print(f"{name} received data: {queue.get(timeout=3)}")
    except Exception as e:
        print("Timeout!", e)


def main_queues2():
    print(" QUEUES 2")
    print(f"Cores Available: {mp.cpu_count()}")

    queue: Queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)

    processes = [Process(target=func, args=(queue,)) for _ in range(5)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


def square_num(identifier: int, num: int, queue: Queue):
    time.sleep(2)
    queue.put((identifier, num**2))


def main_queues3():
    print(" QUEUES 3")
    print(f"Cores Available: {mp.cpu_count()}")

    queue: Queue = Queue()
    data: list[int] = list(range(1, 9))

    processes = [
        Process(target=square_num, args=(identifier, num, queue))
        for identifier, num in enumerate(data)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    unsorted = [queue.get() for _ in processes]
    print(f"Unsorted: {unsorted}")

    result = [val[1] for val in sorted(unsorted)]
    print(f"Sorted: {result}")


def func_sem(p_lock, identifier):
    with p_lock:
        time.sleep(1)
        print(f">> Process {identifier} is running...")


def main_locks_semaphores():
    print(" LOCKS SEMAPHORES")
    print(f"Cores Available: {mp.cpu_count()}")

    lock = Lock()
    sem = Semaphore(3)

    # processes = [Process(target=func_sem, args=(lock, i)) for i in range(5)]
    processes = [Process(target=func_sem, args=(sem, i)) for i in range(5)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    # main_processes()
    # main_pools_map()
    # main_pools_starmap()
    # main_pools_multi_func()
    # main_data_sharing_issue()
    # main_pipes()
    # main_pipes2()
    # main_queues()
    # main_queues2()
    # main_queues3()
    main_locks_semaphores()
    ...
