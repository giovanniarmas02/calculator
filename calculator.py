def add(a,b):
    add_result=a+b
    return add_result

def subtract(a,b):
    sub_result=a-b
    return sub_result

def multiply(a,b):
    mul_result=a*b
    return mul_result

def division(a,b):
    try: 
        div_result=a/b
        return div_result
    except ZeroDivisionError:
        return "Error: cannot divide by 0."

def floor_division(a,b):
    floor_div_result=a//b
    return floor_div_result

def modulo(a,b):
    mod=a%b
    return mod

def exponentiation(a,b):
    exp=a**b
    return exp

while True:
    try:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        operation=input("Choose operation(+, -, *, /, //, %, **): ")
        if operation=="+":
            print(add(num1, num2))
        elif operation=="-":
            print(subtract(num1, num2))
        elif operation=="*":
            print(multiply(num1, num2))    
        elif operation=="/":
            print(division(num1, num2))
        elif operation=="//":
            print(floor_division(num1, num2))
        elif operation=="%":
            print(modulo(num1, num2))
        elif operation=="**":
            print(exponentiation(num1, num2))
        ask=input("Do you want to calculate again? (y/n): ")
        if ask !="y":
            break
    except ValueError:
        print("That's not a valid number.")