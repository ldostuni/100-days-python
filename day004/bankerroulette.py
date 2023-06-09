import random

people = input("Insert a list of people with comma and space separating them: ").split(", ")

choice = random.randint(0, len(people) - 1)

print(f"{people[choice]} will pay the bill!")