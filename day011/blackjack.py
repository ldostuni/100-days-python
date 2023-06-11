import random
from os import system

def add_for_seed(deck, value):
    """Helper function to generate a card for each seed."""
    deck.append({"seed" : "hearts", "value" : value})
    deck.append({"seed" : "spades", "value" : value})
    deck.append({"seed" : "diamonds", "value" : value})
    deck.append({"seed" : "clubs", "value" : value})

def create_deck():
    """Generates a single deck of 52 cards and returns it as an array."""
    deck = []
    for i in range(1, 11):
        add_for_seed(deck, i)

    add_for_seed(deck, "J")
    add_for_seed(deck, "Q")
    add_for_seed(deck, "K")

    return deck

def get_cards(cards, deck, num):
    """Gets a user specified number of cards and removes it from the deck."""
    while num > 0:
        cards.append(deck.pop(0))
        num -= 1
    return cards

def seed(card):
    """Returns the symbol of the seed for the selected card."""
    if card["seed"] == "hearts":
        return "♡"
    if card["seed"] == "spades":
        return "♤"
    if card["seed"] == "diamonds":
        return "♢"
    if card["seed"] == "clubs":
        return "♧"

def show_cards(cards, num_of_cards):
    """Returns the values of the cards of a player's hand."""
    card = ""
    for i in range(0, num_of_cards):
        card += seed(cards[i]) + ":" + str(cards[i]["value"])
        if i != (num_of_cards - 1):
            card += ", "
    return card

def check_value(cards):
    """Calculates the points of a hand and returns it as an integer."""
    total = 0
    has_seed = False
    for card in cards:
        if card["value"] == "J" or card["value"] == "Q" or card["value"] == "K":
            total += 10
        elif card["value"] == 1:
            total += 11
            has_seed = True
        else:
            total += card["value"]
    if has_seed and total > 21:
        total -= 10
    return total



def play_game():
    """Main Blackjack game function."""
    system("cls||clear")
    deck = create_deck()
    random.shuffle(deck)
    player_cards = []
    dealer_cards = []
    new_card = ""
    get_cards(player_cards, deck, 2)
    get_cards(dealer_cards, deck, 2)

    player_total = check_value(player_cards)
    dealer_total = check_value(dealer_cards)
    
    system("cls||clear")
    print(f"Your cards: {show_cards(player_cards, len(player_cards))} (Total = {player_total})")
    print(f"Dealer card: {show_cards(dealer_cards, 1)}")

    if player_total < 21 and dealer_total < 21:
        new_card = input("Get a new card? y or n: ").lower()
    while new_card == "y":
        get_cards(player_cards, deck, 1)
        player_total = check_value(player_cards)
        
        system("cls||clear")
        print(f"Your cards: {show_cards(player_cards, len(player_cards))} (Total = {player_total})")
        print(f"Dealer card: {show_cards(dealer_cards, 1)}")
        if player_total < 21:
            new_card = input("Get a new card? y or n: ").lower()
        else:
            new_card = "n"

    player_total = check_value(player_cards)
    dealer_total = check_value(dealer_cards)

    while dealer_total < 17 and player_total < 21:
        get_cards(dealer_cards, deck, 1)
        dealer_total = check_value(dealer_cards)

    system("cls||clear")
    print(f"Your cards: {show_cards(player_cards, len(player_cards))} (Total = {player_total})")
    print(f"Dealer card: {show_cards(dealer_cards, len(dealer_cards))} (Total = {dealer_total})")

    if (player_total > 21 or dealer_total > player_total) and dealer_total <= 21:
        if dealer_total == 21 and len(dealer_cards) == 2:
            print("Blackjack...you lose...")
        else:
            print("You lose...")
    elif player_total == dealer_total:
        print("A draw.")
    elif player_total > dealer_total or dealer_total > 21:
        if player_total == 21 and len(player_cards) == 2:
            print("Blackjack! You win!")
        else:
            print("You win!")


while input("Do you wanna play a game of Blackjack? y or n: ").lower() == "y":
    play_game()