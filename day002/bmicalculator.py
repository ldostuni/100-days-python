height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2

# print(f"Your bmi is {bmi : .2f}")
print(f"Your bmi is {int(bmi)}")