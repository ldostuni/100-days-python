age = int(input("What is your current age? "))

the_end = 90

remaining_time = the_end - age

days_left = remaining_time * 365
weeks_left = remaining_time * (365 // 7)
months_left = remaining_time * 12

print(f"You have {days_left} days left, {weeks_left} weeks left and {months_left} months left :)")