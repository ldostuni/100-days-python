from math import ceil

# 1 can = 5 square meters of wall

def can_calculator(height, width, cover):
    return ceil(height * width / cover)

height = int(input("How tall is the wall? "))
width = int(input("How wide is the wall? "))

print(f"The wall is {height} * {width} = {height * width}: ")
print(f"You need {int(can_calculator(height, width, cover=5))} cans of paint.")
