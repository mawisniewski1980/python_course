from typing import override, Sequence, TypedDict, Unpack

print("\n PYTHON 3.12")
print("\n OVERRIDE")


class Computer:
    def __init__(self, name: str) -> None:
        self.name = name

    def turn_on(self) -> None:
        print(f'Turning on: {self.name}')

    def turn_off(self) -> None:
        print(f'Turning off: {self.name}')


class Windows(Computer):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    @override
    def turn_on(self) -> None:
        print(f'Turning on my Windows computer!: {self.name}')

    @override
    def turn_off(self) -> None:
        print(f'Turning off my Windows computer!: {self.name}')


cmp1: Computer = Computer("comp1")
cmp1.turn_on()
cmp1.turn_off()

cmp2: Computer = Windows("comp2")
cmp2.turn_on()
cmp2.turn_off()

print("\n TYPE")

type StrOrInt = str | int
type Coordinate = tuple[float, float]
type MySequence[T] = Sequence[T]

print("\n UNPACK")


class Item(TypedDict):
    name: str
    value: float


def info(name:str, /,  **kwargs: Unpack[Item]) -> None:
    print(name, kwargs, sep=': ')


info('Test', name='Pencil', value=100, color='red')