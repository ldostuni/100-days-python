year = int(input("Give me a year: "))

""" if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is NOT a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.") """

by4 = year % 4 == 0
by100 = year % 100 == 0
by400 = year % 400 == 0

calc = (by4 and not(by100)) or (by4 and by100 and by400)

if calc:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")