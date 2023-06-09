numbers = input("How many pretzels did each of my sweet goblins steal? ").split()

count = 0
sum = 0

for num in numbers:
    sum += int(num)
    count += 1

avg = sum / count

print(f"The average pretzelness was {avg} per goblin!")

