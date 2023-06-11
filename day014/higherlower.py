import random

goblins = [{
    "name" : "Gorgon",
    "followers" : 3245,
    "description" : "A rough guy with many edges.",
    "country" : "Gargontan",
},{
    "name" : "Arthos",
    "followers" : 1003,
    "description" : "Cute little gremlin.",
    "country" : "Oronthan",
},{
    "name" : "Ackreth",
    "followers" : 23400,
    "description" : "A singer before everything else.",
    "country" : "Elector",
},{
    "name" : "Mikased",
    "followers" : 3450,
    "description" : "A couple of legs and hands.",
    "country" : "Garath",
}
]

def check_answer(first, second, guess):
    answer = 0
    if first["followers"] > second["followers"]:
        answer = 1
    else:
        answer = 2
    return guess == answer

has_lost = False
points = 0

while has_lost == False and len(goblins) > 0:
    if points == 0: 
        choice1 = goblins.pop(random.randint(0, len(goblins) - 1))
    choice2 = goblins.pop(random.randint(0, len(goblins) - 1))
    print(f"num 1: {choice1['name']}, {choice1['description']} From {choice1['country']}.")
    print("vs")
    print(f"num 2: {choice2['name']}, {choice2['description']} From {choice2['country']}.")

    guess = int(input("Who's got the most followers? "))

    print(f"{choice1['name']} has {choice1['followers']} followers.")
    print(f"{choice2['name']} has {choice2['followers']} followers.")

    if check_answer(choice1, choice2, guess):
        print("You're right!")
        points += 1
        choice1 = choice2
    else:
        print("You're wrong...")
        has_lost = True

print("Your final score is", points)