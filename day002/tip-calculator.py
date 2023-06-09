tip1 = 10
tip2 = 12
tip3 = 15

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
people = input("How many people to split the bill? ")
percentage = input(f"What percentage tip would you like to give? {tip1}, {tip2} or {tip3}? ")

print(f"Each person should pay: ${(float(total_bill) * float(percentage) / 100 + float(total_bill)) / float(people) : .1f}")