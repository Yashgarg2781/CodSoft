calculate=True
a=int(input("Enter first number: "))
while calculate==True:
    print("+,-,*,/")
    operation=input("Choose the operation you want to perform: ")
    b=int(input("Enter next number: "))
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mul(a, b):
        return a * b
    def div(a, b):
        return a / b
    if operation == "+":
        result=add(a,b)
        print(f"{a} {operation} {b} = {result}")
    elif operation=="-":
        result = sub(a, b)
        print(f"{a} {operation} {b} = {result}")
    elif operation == "*":
        result = mul(a, b)
        print(f"{a} {operation} {b} = {result}")
    elif operation == "/":
        result = div(a, b)
        print(f"{a} {operation} {b} = {result}")
    further_operation = input(f"Enter 'y' to continue with {result} or 'n' to start a new calculation or 'x' to exit: ")
    if further_operation == 'y':
        a = result
    elif further_operation == 'n':
        a = int(input("Enter first number: "))
    elif further_operation == 'x':
        calculate = False
        print("Thank you ... Goodbye...")