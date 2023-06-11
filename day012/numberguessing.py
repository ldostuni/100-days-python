import random

print("Welcome to the number guessing game!")
difficulty = input("Choose your difficulty: 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

print(f"You chose {difficulty} difficulty, you have {attempts} attempts.")

mystery_number = random.randint(1, 100)
guess = 0
while guess != mystery_number and attempts > 0:
    guess = int(input("Choose a number between 1 and 100: "))

    if guess > mystery_number:
        print("Too high!")
        attempts -= 1
        print(f"You have {attempts} attempts.")
    elif guess < mystery_number:
        print("Too low!")
        attempts -= 1
        print(f"You have {attempts} attempts.")
    else:
        print(f"The number was {mystery_number}, you won!")

if attempts == 0:
    print(f"The number was {mystery_number}, you lose...")