import random

difficulty_dict = {
    "easy" : 10,
    "hard" : 5,
}

def choose_difficulty(value, diff_dict):
    return diff_dict[value]


def check_attempt(guess, mystery_number, att):
    if guess > mystery_number:
        print("Too high!")
        return att - 1
    elif guess < mystery_number:
        print("Too low!")
        return att - 1
    else:
        print(f"The number was {mystery_number}, you won!")


print("Welcome to the number guessing game!")
difficulty = input("Choose your difficulty: 'easy' or 'hard': ").lower()
attempts = choose_difficulty(difficulty, difficulty_dict)

print(f"You chose {difficulty} difficulty, you have {attempts} attempts.")

mystery_number = random.randint(1, 100)
guess = 0
while guess != mystery_number and attempts > 0:
    guess = int(input("Choose a number between 1 and 100: "))
    attempts = check_attempt(guess, mystery_number, attempts)
    print(f"You have {attempts} attempts.")


if attempts == 0:
    print(f"The number was {mystery_number}, you lose...")