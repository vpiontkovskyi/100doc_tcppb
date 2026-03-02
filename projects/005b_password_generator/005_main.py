"""
A program for generating secure passwords with a customizable mix of letters, symbols, and numbers.
This program allows users to specify how many letters, symbols, and numbers they would like
to include in their password. The input is validated to ensure only whole numbers are accepted.
The generated password is randomized to enhance security.
"""
import random
import string


print("Welcome to the PyPassword Generator!")


"""
Shorter version and as expected in course.
"""

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# nr_letters = int(input("How many letters would you like in your password? "))
# nr_symbols = int(input(f"How many symbols would you like? "))
# nr_numbers = int(input(f"How many numbers would you like? "))
# password_list = []
# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))
# for char in range(1, nr_symbols + 1):
#     password_list.append(random.choice(symbols))
# for char in range(1, nr_numbers + 1):
#     password_list.append(random.choice(numbers))
# random.shuffle(password_list)
# password = "".join(password_list)
# print(password)



"""
As upgrade of this program I propose add validation to input: non empty, non spaces, remove lists and use string module.
"""
LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = string.punctuation
def ask_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Error: please enter a whole number (e.g. 12).")
            continue
        return value
    return True
nr_letters = ask_int("How many letters would you like in your password? ")
nr_symbols = ask_int("How many symbols would you like? ")
nr_numbers = ask_int("How many numbers would you like? ")
password_list = []
for _ in range(1, nr_letters + 1):
    password_list.append(random.choice(LETTERS))
for _ in range(1, nr_symbols + 1):
    password_list.append(random.choice(SYMBOLS))
for _ in range(1, nr_numbers + 1):
    password_list.append(random.choice(NUMBERS))
random.shuffle(password_list)
password = "".join(password_list)
print(password)
