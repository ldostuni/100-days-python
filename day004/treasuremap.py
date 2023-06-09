row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

map = [row1, row2, row3] 

print(f"{row1}\n{row2}\n{row3}")

spot = input('Where do you want to hide the treasure? Use 2 numbers as input: ')

x = int(spot[0]) - 1
y = int(spot[1])

map[-y][x] = "X"


print(f"{row1}\n{row2}\n{row3}")
