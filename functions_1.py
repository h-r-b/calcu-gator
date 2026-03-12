print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
option = int(input("Pick an option (1/2/3/4): "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    if y == 0:
        return "Can't divide by zero"
    return round(x/y, 2)

if option == 1:
    print(add(a, b))
elif option == 2:
    print(sub(a, b))
elif option == 3:
    print(mul(a, b))
elif option == 4:
    print(div(a, b))
else:
    print("Invalid option")