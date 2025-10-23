import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
def calculate(switch, answer):
    if switch:
        n1 = float(input("What is the first number?    "))
        n1 = answer
    user_operations = input("+\n-\n*\n/\nPick an operation     ")
    n2 = float(input("What is the next number?    "))

    return operations[user_operations](n1, n2)
on_switch = True
while True:
    answer = calculate(on_switch, 0)
    print(answer)
# try:
#     if user_operations in operations.keys():
        
#         try:
#             n2 = float(input("What is the next number?    "))

#         except ValueError:
#             print("Please enter a number.")


    go_on = input("Type yes if you want to continue your calculations. Type no to start a new calculation.")

    if go_on == "yes" or "y":
        on_switch = False

    elif go_on == "no" or "n":
        os.system("cls" if os.name == "nt" else "clear")
