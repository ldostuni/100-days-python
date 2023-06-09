import random
import string

symbol_table = "!@#$%^&*()-_=+,<.>/?;:'\"\\|[{}]"

print("Welcome to PyPassword generator!")

letters = input("How many letters would you like in your password? ")
symbols = input("How many symbols? ")
numbers = input("How many numbers? ")

password = ""

for i in range(0, int(letters)):
    password += random.choice(string.ascii_letters)

for i in range(0, int(symbols)):
    password += random.choice(symbol_table)

for i in range(0, int(numbers)):
    password += random.choice("1234567890")

pass_list = list(password)

random.shuffle(pass_list)

shuffled = "".join(pass_list)

print(f"Your password is: {shuffled}")