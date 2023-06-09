import random

choice_str = input("Guess, heads or tails? use H and T: ").lower()
choice = 0 if choice_str == "h" else 1

num = random.randint(0, 1)

if num == 0:
    print("Coin flipped heads: ", end='')
else:
    print("Coin flipped to tails: ", end='')

if bool(num) == bool(choice):
    print("You won!")
else:
    print("You lose...")