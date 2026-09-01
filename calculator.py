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

while True:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operation=input("Choose operation(+, -, *, /): ")
    if operation=="+":
        print(add(num1, num2))
    elif operation=="-":
        print(subtract(num1, num2))
    elif operation=="*":
        print(multiply(num1, num2))    
    elif operation=="/":
        print(division(num1, num2))
    ask=input("Do you want to calculate again? (y/n)")
    if ask !="y":
        break
    