import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

words = ["hobbies","spring","airplane","back","cats"]

lives = 6
has_won = False

word = list(words[random.randint(0, len(words) - 1)])
# word = random.choice(words)
word_guess = []

for i in word:
    word_guess.append("_")

while lives > 0 and not has_won:
    letter_i = 0
    guess_i = 0
    guessed_right = False
    guess = input("Choose a letter: ").lower()
    try:
        letter_i = alphabet.index(guess)
    except:
        letter_i = -1
    if letter_i == -1:
        print("Guess a letter you didn't already guess.")
    else:
        for i in range(0, len(word)):
            if guess == word[i]:
                word_guess[i] = guess
                guessed_right = True
        if not guessed_right:
            lives -= 1
            print(f"You guessed wrong, you have {lives} lives left.")
    alphabet = alphabet.replace(guess, "")
    print(word_guess)
    has_won = not "_" in word_guess

if has_won:
    print("You won!")
    print(f"The word was {''.join(word)}.")
else:
    print("You lose...")
    print(f"The word was {''.join(word)}.")

# you can loop of strings as you would on arrays