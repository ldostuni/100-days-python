numbers = input("Whose of my dear goblins got the most pretzels? ").split()

max_num = 0
index = 0

for num in range(0, len(numbers)):
    if int(numbers[num]) > max_num:
        max_num = int(numbers[num])
        index = num

print(f"The goblin number {index} had {max_num} pretzels with him, golly!")