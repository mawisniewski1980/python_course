from datetime import datetime
from typing import List, Literal, Set, Dict, Tuple, Any, Final, Iterable, Sequence, Callable, Protocol, TypedDict, Required, NotRequired, Generator, Iterator
from sys import getsizeof

print("\n ADVANCING TYPING")
print("\n ADVANCING TYPING")

people: List[str] = ['Mario', 'Luigi']
coordinates: Tuple[int, str] = (1, 'Max')

print("\n ANY")


def display_size(user_input: Any) -> None:
    print(f'{user_input} -> {getsizeof(user_input)} bytes')


display_size([1, 2, 3])
display_size(1000)
display_size("HELLO")
display_size(None)

print("\n FINAL")  # Final FINAL CONSTANT Constants

CONSTANT: Final = 'I am a constant'
CONSTANT2: Final[str] = 'I am a constant'
PI: Final[float] = 3.14
print(CONSTANT)
print(CONSTANT * 2)
print(CONSTANT2)
print(PI)

print("\n ITERABLES")


def list_elements(elements: Iterable) -> None:
    for i, element in enumerate(elements, start=1):
        print(i, element, sep=': ')


def list_elements2(elements: Iterable[str]) -> None:
    for i, element in enumerate(elements, start=1):
        print(i, element.upper(), sep=': ')


people: List[str] = ['Mario', 'Luigi', 'James']
numbers: List[int] = [1, 2, 3]
list_elements(people)
list_elements('Hello')
# list_elements(10) # TypeError: 'int' object is not iterable
list_elements2(people)
#list_elements2(numbers) # AttributeError: 'int' object has no attribute 'upper'


print("\n SEQUENCES")  # ordered TYPE only

sample_list: list[int] = [1, 2, 3]
sample_set: set[int] = {1, 2, 3}  # TypeError: 'set' object is not subscriptable

print(sample_list)
print(sample_list)
print(sample_list)
print(sample_set)
print(sample_set)
print(sample_set)


def get_first_element(sequence: Sequence[int]) -> int:
    return sequence[0] if sequence else -1


print(get_first_element(sample_list))
# print(get_first_element(sample_set)) # TypeError: 'set' object is not subscriptable

print("\n CALLABLES")


def get_time() -> str:
    return f'{datetime.now():%H:%M:%S}'


print(get_time())


def repeat(func: Callable, amount: int) -> None:
    for i in range(amount):
        print(f'{i + 1}: {func()}')


repeat(get_time, 3)


def print_it(text: str, print_func: Callable[[str], None]) -> None:
    print_func(text)


def loud_print(text: str) -> None:
    print(f'{text.upper()}!')


def silent_print(text: str) -> None:
    print(f'({text.lower()})')


print_it("hello", loud_print)
print_it("hello", silent_print)

print("\n PROTOCOLS")  # define the structure of what a class should like  INTERFACE in JAVA


class Printer(Protocol):
    def print(self, magazine: str) -> None:
        ...

    def copy(self, magazine: str, copies: int) -> None:
        ...


class LazerPrinter:

    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version

    def print(self, magazine: str) -> None:
        print(f'{self.name} ({self.version}) is printing: "{magazine}".')

    def copy(self, magazine: str, copies: int) -> None:
        print(f'{self.name} ({self.version}) is making {copies} copies of: "{magazine}".')


class InkJetPrinter:

    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version

    def print(self, magazine: str) -> None:
        print(f'{self.name} ({self.version}) is printing: "{magazine}".')

    def copy(self, magazine: str, copies: int) -> None:
        print(f'{self.name} ({self.version}) is making {copies} copies of: "{magazine}".')


lp: Printer = LazerPrinter('Lazer Printer', 1)
lpi: Printer = InkJetPrinter('InkJet Printer', 10)


def print_magazine(printer: Printer, magazine: str) -> None:
    printer.print((magazine))
    print('Performing extra logic')
    printer.copy(magazine, 5)
    print('Shutting down printer...')


print_magazine(lp, 'Python Times')
print()
print_magazine(lpi, 'Geeks of Python')

print("\n TYPEDDICT")


class Coordinate(TypedDict):
    x: float
    y: float
    label: str
    category: NotRequired[str]


coordinate1: Coordinate = {'x': 20, 'y': 10, 'label': 'Profit'}
coordinate2: Coordinate = {'x': 20, 'y': 10, 'label': 'Profit', 'category': 'Finance'}

Vote = TypedDict('Vote', {'for': int, 'against': int}, total=False)

vote1: Vote = {'for': 100}
vote2: Vote = {'for': 100, 'against': 200}
vote3: Vote = {'against': 200}

Vote2 = TypedDict('Vote',
                  {'for': int,
                   'against': int,
                   'topic': Required[str]},
                  total=False)

vote4: Vote2 = {'for': 100, 'against': 200, 'topic': 'More money'}
vote5: Vote2 = {'topic': 'More money'}

print(vote1)
print(vote2)
print(vote3)
print(vote4)
print(vote5)

from typing import Literal, TypeAlias, Callable, NewType, Self

print("\n LITERALS")

Mode = Literal['r', 'w', 'a']


def read_file(file: str, mode: Mode) -> None:
    print(f'Reading {file} in "{mode}" mode.')


read_file('xx.txt', 'r')
read_file('xx.txt', 'w')
read_file('xx.txt', 'a')
read_file('xx.txt', 'Z')

print("\n TYPE ALIAS")

OptionalStr: TypeAlias = str | None
Mode: TypeAlias = Literal['r', 'w', 'a']
Printer: TypeAlias = Callable[[str], str]


def func(text: OptionalStr):
    ...


FruitType: TypeAlias = 'Fruit'


class Fruit:
    def __init__(self, name: str) -> None:
        self.name = name

    def fruit_method(self) -> FruitType:
        return self


orange: Fruit = Fruit('orange')
orange.fruit_method()

print("\n NEW TYPE")

UserId = NewType('UserId', int)


def get_user(userid: UserId) -> str | None:
    users: dict = {0: 'Mario', 1: 'James', 2: 'Luigi'}
    return users.get(userid)


print(get_user(0))
print(get_user(False))
print(get_user(UserId(0)))
print(0 == UserId(0))

print("\n SELF")


class File:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    @classmethod
    def create_file(cls, name: str, ext: str) -> Self:
        return cls(f'{name}.{ext}')

    def __enter__(self) -> Self:
        print(f'Opening "{self.filepath}"')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        print(f'Closing "{self.filepath}"...')


file: File = File.create_file('cat', 'jpg')
print(file.filepath)

with File('cat.jpg') as file:
    print(file.filepath)


class JPEG(File):
    def jpeg_method(self) -> Self:
        print('Doing something jpeg releated...')
        return self


jpeg: JPEG = JPEG.create_file('dog', 'png')
jpeg.jpeg_method()

print("\n GENERATORS")


def generate() -> Generator[int, int, str]:
    for i in range(3):
        yield i

    return 'SOME_VALUE'


numbers: Generator[int, int, str] = generate()
print(next(numbers))
print(numbers.send(10))
print(next(numbers))


def generate2() -> Iterator[int]:
    for i in range(3):
        yield i


numbers2: Iterator[int] = generate2()
print(next(numbers2))
print(next(numbers2))
print(next(numbers2))
print(next(numbers2))
