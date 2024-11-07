# IF ELSE
print(" IF ELSE")

a = 10
if a > 5:
    print(a, a > 5, "a > 5")
else:
    print(a, a < 5, "a < 5")

text = "hello"
if text == "hello":
    print("Bot: HELLO!")
elif text == "bye":
    print("Bot: Goodbye!")
else:
    print("Bot: I did not understand...")

# SHORTHAND IF...ELSE
# do this if TRUE else do this
print("Success") if 1 > 2 else print("Failure")
a, b = 10, 20
print("a is greater") if a > b else print("b is greater")
result = a if a > b else b
print(result)

# FOR LOOP
print("\n FOR LOOP")
people = ["Mario", "Luigi", "Peach", "Toad"]
for i, person in enumerate(people, 1):
    print(i, person)

numbers = range(0, 5)
for number in numbers:
    print(number)
print("\n")

for number in range(5):
    print(number)
print("\n")

for x in "Mario":
    print(x)

# WHILE LOOP
print("\n WHILE LOOP")

a = 0
while a < 5:
    print(a, "Hello")
    a += 1

# BREAK CONTIUNUE
print("\n BREAK for")

for i in range(10):
    print(i)

    if i == 5:
        break

print("\n BREAK while")

i = 0
while i < 3:
    print(i)

    if i == 1:
        break

    i += 1

print("\n CONTIUNUE for")
for i in range(5):
    if i == 3:
        continue

    print(i)

print("\n CONTIUNUE BREAK for")
for i in range(5):
    if i == 3:
        continue

    if i == 4:
        break

    print(i)

# PASS
print("\n PASS - perform nothing")
a, b = 10, 20

if a > b:
    # Do this thing
    pass

for i in range(10):
    pass

# LOOP...ELSE
print("\n LOOP...ELSE for")

for i in range(5):
    print(i, end=" ")
else:
    print("SUCCESS!!")


for i in range(5):
    print(i, end=" ")

    if i == 2:
        break
else:
    print("SUCCESS !!!")

print("\n LOOP...ELSE while")
i = 0
while i < 3:
    print(i, end=" ")
    i += 1
else:
    print("SUCCESS!!")

i = 0
while i < 3:
    print(i, end=" ")
    i += 1
    if i == 2:
        break
else:
    print("SUCCESS !!!")
