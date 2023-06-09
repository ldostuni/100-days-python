import random

choice = int(input("What do you choose? 1 for rock, 2 for paper, 3 for scissors: ")) - 1

cpu = random.randint(0, 2)

choices = ["rock", "paper", "scissors"]

print(f"You: {choices[choice]}")
print(f"CPU: {choices[cpu]}")

if choices[choice] == choices[cpu]:
    print("It's a tie!")
elif choices[choice - 1] == choices[cpu]:
    print("You win!")
elif choices[choice] == choices[cpu - 1]:
    print("You lose...")

