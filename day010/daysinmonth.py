def is_leap_year(year):
    """
    This function checks whether the year is a leap year or not.
    """
    by4 = year % 4 == 0
    by100 = year % 100 == 0
    by400 = year % 400 == 0

    calc = (by4 and not(by100)) or (by4 and by100 and by400)

    if calc:
        return True
    else:
        return False
    
def days_in_month(year, month):
    '''
    This function returns the days in a month, checking whether it's a leap year or not.
    '''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[1] = 29
    return month_days[month - 1]

cont = "yes"

while cont == "yes":
    year = int(input('Give me a year: '))
    month = int(input('Give me a month: '))

    days = days_in_month(year, month)

    print(f"There's {days} days in month number {month}, year {year}.")
    cont = input("Continue? yes or no: ").lower()