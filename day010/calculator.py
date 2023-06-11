
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# def calculate(a, b, operator):
#     if operator == "+":
#         return add(a, b)
#     elif operator == "-":
#         return subtract(a, b)
#     elif operator == "*":
#         return multiply(a, b)
#     elif operator == "/":
#         return divide(a, b)
#     else:
#         return add(a, b)

new_calc = "n"

while True:
    if new_calc != "y":
        num1 = float(input("What's the first number? "))
    for op in operations:
        print(op)
    # print("=\n-\n*\n/")
    operator = input("Pick your poison: ")
    num2 = float(input("Pick your next number: "))
    calculate = operations[operator]
    result = calculate(num1, num2)

    print(f"{num1 :.2f} {operator} {num2 :.2f} = {result :.2f}")
    new_calc = input(f"Type 'y' to continue calculating with {result :.2f}, or type 'n' to start a new calculation.")
    if new_calc == "y":
        num1 = result
 
