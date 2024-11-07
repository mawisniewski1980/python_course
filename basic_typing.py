from typing import Union, Optional
import requests
from requests import Response

print("\n BASIC TYPES")

text: str = "hello"
number: int = 10
percent: float = 0.50
connected: bool = False


def format_input(user_input: str):
    print(user_input.capitalize())


format_input("hello world")

print("\n UNION TYPES")

var: str | int = 10
var2: Union[str, int] = 10


def func(user_input: str | int):
    print(user_input)


func("text")
func(10)

print("\n LISTS")

elements: list = [1, 2, 3, 4, 5]
elements2: list[int] = [1, 2, 3, 4, 5]
mixed: list[int | str] = ["a", 1]
nested: list[list[str]] = [["a", "b"], ["c", "d"]]
uncaught_list: list[str] = [10, None, "hello"]  # pycharm nie zwróci błędu - UWAGA

print("\n TUPLES")

cordinates: tuple = (20, 30)
cordinates2: tuple[int, int] = (20, 30)
cordinates3: tuple[str, int, bool] = ("hello", 30, True)
cordinates4: tuple[int, ...] = (
    1,
    2,
    3,
    4,
    5,
)  # tuple  z intami nie okreslonej dlugosci

print("\n SETS")

my_set: set = {1, 2, 3}
my_set2: set[str] = {"1", "2", "3"}
my_set3: set[str | int] = {"1", 2, "3"}

print("\n DICTIONARIES")

my_dict: dict[str, int] = {"a": 10, "b": 11}


def print_it(some_dict: dict[int, str]):
    for value in some_dict.values():
        print(value.title())


xxx: dict[int, str] = {1: "a", 2: "b", 3: "c"}
print_it(xxx)

print("\n OPTIONALS")

person: str | None = "Luigi"
person2: str | None = None
person3: Optional[str] = None


def greet_person(name: str | None = None):
    if name is None:
        print('No one is here...')
    else:
        print(f'Hello, {name}')


greet_person()
greet_person('Max')

print("\n CLASSES")


class Fruit:
    def __init__(self, name: str, grams: float):
        self.name = name
        self.grams = grams


orange: Fruit = Fruit('Orange', 100)


def describe(fruit: Fruit):
    print(f'{fruit.name} weighs {fruit.grams} grams')


describe(orange)


class Apple(Fruit):
    ...


apple: Apple = Apple('Fuji Apple', 50)
describe(apple)

print("\n RETURN TYPES")


def add_numb(a: int, b: int) -> int:
    return a + b


def hack_nasa() -> None:
    print('Hacking...')


def fetch_user(user_id: int) -> str | None:
    users: dict = {0: 'Mario', 1: 'Luigi'}
    return users.get(user_id)


print(add_numb(10, 10))
print(hack_nasa())
print(fetch_user(1))
print(fetch_user(4))

print("\n EXTERNAL TYPES")

def get_status(url: str) -> int:
    # request = requests.get(url)
    request: Response = requests.get(url)
    status_code: int = request.status_code
    return status_code

def analyse_response(response: Response) -> None:
    print(response.content)

print(get_status('https://www.apple.com'))

request: Response = requests.get('https://www.apple.com')
print(analyse_response(request))


print("\n HOMEWORK")

# Exercise 1
text: str = 'Hello, world!'
percent: float = 3.14
is_connected: bool = False
people: list[str] = ['Mario', 'Luigi', 'James']


# Exercise 2
class Fruit:
    def __init__(self, name: str, grams: int) -> None:
        self.name = name
        self.grams = grams


def return_fruit_description(fruit: Fruit) -> str:
    return f'This {fruit.name} weighs {fruit.grams} grams.'


apple = Fruit('Apple', 50)
description = return_fruit_description(apple)
print(description)


# Exercise 3
def get_user(user_id: int) -> str | None:
    users: dict[int, str] = {0: 'Mario', 1: 'Luigi'}
    return users.get(user_id)


first_user: str | None = get_user(0)
print(first_user)
