# varialble
greeting = "Hello "

print(greeting + "Mario")
print(greeting + "Luigi")

# types and type hint
print("\n")
name: str = "Mario"  # string - immutable
number: int = 100  # int 100, -100 ...
decimal: float = 0.5  # float
com: complex = 8j  # complex

poeple: list[str] = ["Mario", "Luigi"]  # list
lotto: tuple = (1, 2, 3, 4, 5, 6)  # tuple - immutable
numbers: range = range(1, 1000)  # range 1 .. 999
users: dict = {"user1": "mario", "user2": "luigi"}  # dictionary
uniqe_nmb: set = {
    1,
    2,
    2,
    3,
    3,
    4,
}  # set - unique elements - not track order - can change
uniqe_nmb_2: frozenset = frozenset({1, 2, 2, 3, 3, 4})  # set
is_conn: bool = True  # bool True 1 False 0
# bytes bytearray memoryview
is_empty: None = None  # no value
print(is_empty)

# type conversion
print("\n type conversion")
result: str = name + str(number)
print(result)
print(type(result))
print(float(number))
print(complex(number))

# INTEGERS
print("\n")
a: int = 1
b: int = 100
c: int = 1000000000000000000000000
c2: int = 100_000_000_000_000_000_000_000_0
d: int = -100
print(a + b + c)
print(c2)

# BASIC OPERATORS
print("\n BASIC OPERATORS")
print(1 + 2)
print(1 - 2)
print(2 * 2)
print(2 / 2)
print(2 / 0.5)
print(10 % 3)  # modulos
print(10**3)  # power do potegi
print(10 // 3)

a = 5
a += 3  # a = a + 3
print(a)

# COMPARSE OPERATORS
print("\n COMPARSE OPERATORS")
print(10 == 5)
print(10 == 10.0)
print(10 == 10)
print(10 != 10)
print(10 < 5)
print(10 > 5)
print(10 >= 5)
print(10 <= 5)

a = 5
b = 10
print(a < b and 10 > 6)
print(a < b and 4 > 6)
print(a < b or 10 > 6)
print(not (a < b or 10 > 6))

a = 100.0
b = 1.0 * a
print(id(a))
print(id(b))
print(a is a)
print(b is b)
print(a == b)
print(a is b)  # comaring identity
print(a is not b)  # comaring identity

numbers = [1, 2, 3, 4, 5]
print(1 in numbers)
print(6 in numbers)
print(6 not in numbers)

# STRINGS
text = "Mario 'this'\nthis "
text2 = """
Jo 
jO 

jo
"""
print(text)
print(text2)

# F STRINGS
print("\n")
text = "text"
print(f"1 {text} 2 {a + b}")

# BOOLEANS
print("\n")
ok = True
nok = False
print(ok)
print(nok)
print(ok == 1)
print(nok == 0)
print(True + True)
print(False + False)

# LISTS
print("\n LISTS")
people: list[str] = [
    "Mario",
    "Luigi",
    "Peach",
    "Toad",
]  # ["Mario", "Luigi", "Peach", "Toad", 10, True]
print(people)
print(len(people))
print(people[0])
print(people[-1])
print(people[0:2])
print(people[0:3])
print(people[0:4])
print(people[2:4])
print("Luigi" in people)
print("luigi" in people)
people[0] = "Shy Guy"
print(people)
people[0:2] = ["Shy Guy", "Bowser"]
print(people)
people.insert(1, "Luigi")  # insert na indeks
people.insert(0, "Mario")  # insert na indeks
print(people)
people.append("BLE BLE")  # doda na koncu
print(people)

people2: list[str] = ["Sonic", "Tails"]
people.extend(people2)
print("\n")
print(people)
print(people2)

people.remove("Shy Guy")
people.remove("Bowser")
people.pop(4)
print(people)
people.reverse()
print(people)
people.sort()
print(people)

# TUPLES duplicates OK, immutable, mix datatype
print("\n TUPLES duplicates OK, immutable, mix datatype")
peoplet: tuple = "Mario", "Luigi", "Peach", "Toad"
people2t: tuple = ("Mario", "Luigi", "Peach", "Toad")
people3t: tuple = ("Mario",)

print(type(peoplet), type(people2t), type(people3t))
print(peoplet[0])
print(peoplet[2:4])
print(peoplet[2:])
print(peoplet[:2])
print("Mario" in peoplet)

print(peoplet.count("Mario"))
print(peoplet.index("Toad"))

# unpacing
a, b, c, d = peoplet
print(a, b, c, d)

a, *b = peoplet  # jeden element + lista z reszta
print(a, b)

# SETS DUPLICATES NOK, UNORDERED
print("\n SETS DUPLICATES NOK, UNORDERED")

items: set = {"apple", "banana", 10, True, 10, True, False}
items2: set = {100, 200, 10, "apple"}
print(items)
print(len(items))
items.add("orange")
print(items)
print(len(items))
items.update(["carrot", 15, 10])
print(items)
print(len(items))

new_set = items.union(items2)
print(new_set)
print(len(new_set))

new_set2 = items | items2
print(new_set2)
print(len(new_set2))

the_same_in_both_set = items.intersection(items2)
print(the_same_in_both_set)
print(len(the_same_in_both_set))

differences = items.symmetric_difference(items2)
print(differences)
print(len(differences))

empty_set = set()  # EMPTY SET
print(empty_set)
print(len(empty_set))

# DICTIONARIES
print("\n DICTIONARIES")
users: dict = {
    "user1": "Mario123",
    "user2": "Luigi123",
    "items": {"apple": 10, "banana": 20},
}
print(users, len(users), type(users))

users1 = users["user1"]
print(users1, len(users1), type(users1))

users1 = users.get("user1")
print(users1, len(users1), type(users1))

print(users.get("X"))

k = users.keys()
print(k, type(k))
v = users.values()
print(v, type(v))
i = users.items()
print(i, type(i))

# convert to list or tuple from dict_keys
l = list(v)
print(l, type(l))

# add to list
users.update({"hello": 123})
print(users, len(users), type(users))
users.pop("hello")
print(users, len(users), type(users))
# users.popitem() # remove last added item
print(users, len(users), type(users))
print(users["items"]["apple"])

print(users.setdefault("user1", "There is no key!"))
print(users.setdefault("user10", "There is no key!"))

# FORMATTING SHORTCUT
