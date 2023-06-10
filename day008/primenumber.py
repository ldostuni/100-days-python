number = int(input("Give me a number: "))

cont = 2

is_prime = True

while cont < number and is_prime:
    if number % cont == 0:
        is_prime = False
    cont += 1

if is_prime:
    print("The number is prime.")
else:
    print("The number is NOT prime.")

###

def is_prime(number):
    is_prime = True
    cont = number - 1
    while cont > 2 and is_prime:
        if number % cont == 0:
            is_prime = False
        cont -= 1