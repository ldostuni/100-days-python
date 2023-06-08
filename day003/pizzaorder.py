print("Welcome to pizza deliveries!")
size = input("What size pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N --> ") == "Y"
extra_cheese = input("Do you want extra cheese? Y or N --> ") == "Y"

bill = 0
small = False

if size == "S":
    bill = 15
    small = True
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni:
    if small:
        bill += 2
    else:
        bill += 3

if extra_cheese:
    bill += 1

print(f"Your bill is ${bill : .2f}")

