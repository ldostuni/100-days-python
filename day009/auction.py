from os import system

print("Welcome to the secret auction program.")

bids = []

other_bidders = "yes"

def add_new_bid(name, bid):
    new_bid = {}
    new_bid["name"] = name
    new_bid["bid"] = bid
    bids.append(new_bid)

def check_bids(bids):
    winner_index = 0
    for i in range(0, len(bids)):
        if bids[i]["bid"] > bids[winner_index]["bid"]:
            winner_index = i
    winner = bids[winner_index]
    print(f"The winner is {winner['name']} with a bid of ${winner['bid']}.")

while other_bidders == "yes":
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    add_new_bid(name, bid)
    other_bidders = input("Are there any othe bidders? Yes or no: ").lower()
    system("cls||clear")

check_bids(bids)