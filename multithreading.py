import threading
import time


# print("hello")
#
# for i in range(5):
#     print("Goodbye")
#
#
def process_data(name: str, count: int):
    print(f"Starting {name}...")

    for i in range(count):
        print(name, i + 1, sep=": ")
        time.sleep(1)


lock = threading.Lock()


def counter(limit: int, name: str):
    for i in range(limit):
        time.sleep(0.5)
        print(name, i + 1, sep=": ")


def task1():
    lock.acquire()
    counter(5, "T-1")
    lock.release()


def task2():
    lock.acquire()
    counter(5, "T-2")
    lock.release()


def task3():
    counter(5, "T-3")


def main_locks():
    # LOCKS
    print("\n LOCKS")

    thread = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    thread3 = threading.Thread(target=task3)

    thread.start()
    thread2.start()
    thread3.start()


def main_multi():
    # MULTITHREADING
    print(" MULTITHREADING")

    process_data("Thread-1", 5)
    process_data("Thread-2", 10)

    thread_one = threading.Thread(target=process_data, args=("Thread-1", 5))
    thread_two = threading.Thread(target=process_data, args=("Thread-2", 5))

    thread_one.start()
    time.sleep(3)
    thread_two.start()

    thread_one.join()
    thread_two.join()


def infinite_loop():
    while True:
        print(time.time())
        time.sleep(1)


def main_daemon():
    # DAEMON THREADS
    print(" DAEMON THREADS")
    thread = threading.Thread(target=infinite_loop, daemon=True)
    thread.start()


sem = threading.Semaphore(5)


def process_something(id: int):
    sem.acquire()
    print(f"{id} -> Running!")
    time.sleep(5)
    print(f"{id} -> Finished!")
    sem.release()


def main_semaphores():
    # SEMAPHORES - How many LOCSK we give to thread
    print(" SEMAPHORES")
    for i in range(10):
        time.sleep(0.5)
        thread = threading.Thread(target=process_something, kwargs={"id": i + 1})
        thread.start()


def process_something_with(id: int):
    with sem:
        print(f"{id} -> Running sem!")
        time.sleep(5)
        print(f"{id} -> Finished sem!")

    with lock:
        print(f"{id} -> Running lock!")
        time.sleep(1)
        print(f"{id} -> Finished lock!")


def main_with_lock_semaphore():
    # WITH LOCK SEMAPHORE
    print(" WITH LOCK SEMAPHORE")
    for i in range(10):
        time.sleep(0.5)
        thread = threading.Thread(target=process_something_with, kwargs={"id": i + 1})
        thread.start()


def edit_bad(operation: str, amount: int, repeat: int):
    global value

    for _ in range(repeat):
        temp: int = value
        time.sleep(0)
        if operation == "add":
            temp += amount
        elif operation == "substract":
            temp -= amount

        time.sleep(0)
        value = temp


def edit_ok(operation: str, amount: int, repeat: int):
    global value

    lock.acquire()
    for _ in range(repeat):
        temp: int = value
        time.sleep(0)
        if operation == "add":
            temp += amount
        elif operation == "substract":
            temp -= amount

        time.sleep(0)
        value = temp

    lock.release()


def main_race_conditions_bad():
    # RACE CONDITIONS - occurs whet two threads access a shared variable at the same time
    print(" RACE CONDITIONS BAD")
    adder = threading.Thread(target=edit_bad, args=("add", 100, 1_000_000))
    substractor = threading.Thread(target=edit_bad, args=("substract", 100, 1_000_000))

    adder.start()
    substractor.start()

    print("Waiting for threads to finish...")

    adder.join()
    substractor.join()

    print(f"{value = }")


def main_race_conditions_ok():
    # RACE CONDITIONS - occurs whet two threads access a shared variable at the same time
    print(" RACE CONDITIONS OK")
    adder = threading.Thread(target=edit_ok, args=("add", 100, 1_000_000))
    substractor = threading.Thread(target=edit_ok, args=("substract", 100, 1_000_000))

    adder.start()
    substractor.start()

    print("Waiting for threads to finish...")

    adder.join()
    substractor.join()

    print(f"{value = }")


if __name__ == "__main__":
    # main_multi()
    # main_locks()
    # main_daemon()
    # main_semaphores()
    # main_with_lock_semaphore()
    value: int = 0
    main_race_conditions_bad()
    value: int = 0
    main_race_conditions_ok()
