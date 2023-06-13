coffees = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "price": 1.50,
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2.50,
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 3.00,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0.0,
}

coins = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.10,
    "quarters": 0.25,
}


def get_coffee_choices(coffee_list):
    coffee_choices = ""
    for name in coffee_list:
        coffee_choices += name
        if name != list(coffee_list)[-1]:
            coffee_choices += "/"
    return coffee_choices


def show_resources(res):
    print(f"Water: {str(res['water'])} ml")
    print(f"Coffee: {str(res['coffee'])} g")
    print(f"Milk: {str(res['milk'])} ml")
    print(f"Money: ${str(res['money'])}")


def check_resources(res, choice):
    coffee = coffees[choice]
    enough_water = True
    enough_coffee = True
    enough_milk = True

    if res["water"] < coffee["water"]:
        enough_water = False
    if res["coffee"] < coffee["coffee"]:
        enough_coffee = False
    if res["milk"] < coffee["milk"]:
        enough_milk = False

    return {"water": enough_water, "coffee": enough_coffee, "milk": enough_milk,}


def make_exchange(choice):
    resources["water"] -= coffees[choice]["water"]
    resources["coffee"] -= coffees[choice]["coffee"]
    resources["milk"] -= coffees[choice]["milk"]
    resources["money"] += coffees[choice]["price"]


def calculate_money(coin_values, coins_given, choice):
    total = 0
    for coin in coins_given:
        total += coins_given[coin] * coin_values[coin]
    return total


def ask_coffee(choice):
    choices = get_coffee_choices(coffees)
    has_resources = {}
    coins_given = {}
    given_money = 0.0
    has_all_resources = True
    if choice != "report":
        coffee_chosen = coffees[choice]
        has_resources = check_resources(resources, choice)

        if not has_resources["water"]:
            print("Sorry, there's not enough water.")
            has_all_resources = False
        if not has_resources["coffee"]:
            print("Sorry, there's not enough coffee.")
            has_all_resources = False
        if not has_resources["milk"]:
            print("Sorry, there's not enough milk.")
            has_all_resources = False

        if has_all_resources:
            coins_given["quarters"] = int(input("How many quarters? "))
            coins_given["dimes"] = int(input("How many dimes? "))
            coins_given["nickels"] = int(input("How many nickels? "))
            coins_given["pennies"] = int(input("How many pennies? "))
            given_money = calculate_money(coins, coins_given, choice)
            print(f"You gave ${given_money : .2f}.")
            if coffee_chosen["price"] > given_money:
                print("Sorry, you don't have enough money.")
            else:
                make_exchange(choice)
                print(f"Here's your {choice.title()} and {given_money - coffee_chosen['price'] : .2f} of change.")
    elif choice == "report":
        show_resources(resources)

    # if choice = "report", show report of all the machine resources
    # method to check if resources are enough for client request
    # if asks for one of coffees, asy "Please insert coins" and for each kind of coin, ask how many
    # give change too
    # if not enough of one resource, say sorry there's not enough x, and ask again what they want


customer_choice = input(f"Welcome, which coffee would you like? ({get_coffee_choices(coffees)}): ").lower()

while customer_choice != "off":
    ask_coffee(customer_choice)
    customer_choice = input(f"Welcome, which coffee would you like? ({get_coffee_choices(coffees)}): ").lower()
