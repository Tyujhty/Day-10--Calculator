# Functions of calculator

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the seconde number?: "))

for operator in operations:
    print(operator)


answer = 0
operation_symbole = input("Pick an operation from the line above: ")

def calculate(num1, num2, operation_symbole):
    answer = operations[operation_symbole](num1, num2)
    return answer

calculate(num1, num2, operation_symbole)

print(f"{num1} {operation_symbole} {num2} = {answer}")