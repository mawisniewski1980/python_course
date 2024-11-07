# CREATING FUNCTION
print(" CREATING FUNCTION")


def greet(name: str):
    print(f"Hey, {name} !")


def do_something():
    for i in range(3):
        print(i, " doing something")
    print("done!")


greet("Mario")
do_something()

# PARAMETERS AND ARGUMENTS
print("\n PARAMETERS AND ARGUMENTS")


def greet2(name: str, greeting: str = "Hello"):
    print(f"{greeting}, {name}")


def greet3(name: str, greeting: str = "Hello", age: int = 0):
    print(f"{greeting}, {name}, {age}")


greet2("Mario")
greet2("Mario", "Cześć")
greet3("Mario", age=18)
greet3(age=18, greeting="JO JO", name="Mario")

# RETURNING FROM A FUNCTION
print("\n RETURNING FROM A FUNCTION")


def sum_numbers(a: int, b: int) -> int:
    return a + b


s = sum_numbers(10, 20)
print(s)

# RECURSION
print("\n RECURSION")


def do_s(n: int):
    print(n)
    if n == 1:
        print("Done")
        return

    do_s(n - 1)


do_s(3)


# ARGS
print("\n  *ARGS")


def greet_people(*people: str):
    print(people, type(people))
    for name in people:
        print(f"Hello {name}")


greet_people("Mario", "Luigi")

# KWARGS
print("\n  **KWARGS")


def do_a(**kwargs):
    print(kwargs, type(kwargs))


do_a(name="Mario", age=10)

# ARGS KWARGS
print("\n  *ARGS **KWARGS")


def do_b(*args, **kwargs):
    print("ARGS: ", args, type(args), "KWARGS: ", kwargs, type(kwargs))


do_b("Max", "Zyzio", name="Mario", age=10)


# ASTERISK SLASH
def std_arg(arg):
    print(arg)


def position_only_arg(arg, arg2, /):
    print(arg, arg2)


def key_world_only_arg(*, arg, arg2):
    print(arg, arg2)


def combined_example(poz_only, poz_only2, /, standard, standard2, *, kwd_only):
    print(poz_only, poz_only2, standard, standard2, kwd_only)


std_arg(10)
position_only_arg(10, 100)
key_world_only_arg(arg=20, arg2=200)
combined_example(1, 2, 3, standard2=4, kwd_only=5)
