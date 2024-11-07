# TRY EXCEPT
print(" TRY EXCEPT")

user_input = input("Enter a number: ")

try:
    number = float(user_input)
    result = number / 0
    print(number)
# except Exception as e:
except ValueError as e:
    print("Please enter a valid number!")
    print(e)
except ZeroDivisionError as e:
    print("Please do not divide by 0!")
except Exception as e:
    print("LOJESU", e)

# TRY EXCEPT ELSE FINALLY
print("\n TRY EXCEPT ELSE FINALLY")


user_input = input("You: ")

try:
    number = float(user_input)
    print(number)
except Exception as e:
    print("Exception", e)
else:
    print("Success executed code")
finally:
    print("Finally")


# RAISE
print("\n RAISE")

user_input: str = input("You: ")

if user_input == "0":
    raise Exception("EXCEPECTION, please never user 0")

is_connection: bool = False


def connected_to_internet():
    if not is_connection:
        raise ConnectionError("No internet!")
    else:
        print("Connceted to the internet")


try:
    connected_to_internet()
except ConnectionError as e:
    print("There is no connection!", e)
except Exception as e:
    print(e)
