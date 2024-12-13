print('Unpacking Sequences (Lists/Tuples)')

print('Example with a tuple')
numbers = (1, 2, 3)
a, b, c = numbers

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

print('Using * to unpack remaining values')
numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers

print(a)  # Output: 1
print(b)  # Output: 2
print(rest)  # Output: [3, 4, 5]

a, *middle, c = numbers
print(a)  # Output: 1
print(middle)  # Output: [2, 3, 4]
print(c)  # Output: 5

print('Unpacking Dictionaries')
print('Example with keys')
data = {'x': 10, 'y': 20}
a, b = data
print(a)  # Output: 'x'
print(b)  # Output: 'y'

print('Example with items')
for key, value in data.items():
    print(key, value)

print('Nested Unpacking')
pairs = [(1, 2), (3, 4), (5, 6)]
for a, b in pairs:
    print(a, b)
# Output:
# 1 2
# 3 4
# 5 6

print('Unpacking with Functions')
print('Example with a list')


def add(a, b):
    return a + b


nums = [1, 2]
print(add(*nums))  # Output: 3

print('Example with a dictionary')
data = {'a': 5, 'b': 10}
print(add(**data))  # Output: 15

print('USwapping Variables')
a, b = 1, 2
a, b = b, a
print(a, b)  # Output: 2, 1
