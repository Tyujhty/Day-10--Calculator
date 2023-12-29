from art import logo

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
def calculate(num1, num2, operation_symbole):
    return operations[operation_symbole](num1, num2)

print(logo)

num1 = float(input("What is the first number?: "))
num2 = float(input("What is the seconde number?: "))

for operator in operations:
    print(operator)

answer = 0
operation_symbole = input("Pick an operation from the line above: ")

answer = calculate(num1, num2, operation_symbole)

print(f"{num1} {operation_symbole} {num2} = {answer}")

continue_calculate = True

while continue_calculate == True:
    
    continue_calculate = input(f"Type 'y' to continue with {answer}, or type 'n' to quit.: ").lower()
    
    if continue_calculate == 'y':
        num1 = answer
        operation_symbole = input("Pick a symbole: ")
        num2 = float(input("Pick a number: "))
        
        answer = calculate(num1, num2, operation_symbole)
        print(f"{num1} {operation_symbole} {num2} = {answer}")
        continue_calculate = True
    else:
        print("Goodbye")