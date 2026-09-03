import math


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
    exp=math.pow(a,b)
    return exp

def square_root(a):
    squ=math.sqrt(a)
    return squ

def greatest_commun_divisor(a,b):
    a=int(a)
    b=int(b)
    gcd=math.gcd(a,b)
    return gcd

def inputs_function(num1, num2):
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    return num1, num2

num1=0
num2=0
while True:
    try:
        operation=input("Choose operation(+, -, *, /, //, %, **, sqr, gcd): ")
        if operation=="+":
            num1, num2 = inputs_function(num1,num2)
            print(add(num1, num2))
        elif operation=="-":
            num1, num2 = inputs_function(num1,num2)
            print(subtract(num1, num2))
        elif operation=="*":
            num1, num2 = inputs_function(num1,num2)
            print(multiply(num1, num2))    
        elif operation=="/":
            num1, num2 = inputs_function(num1,num2)
            print(division(num1, num2))
        elif operation=="//":
            num1, num2 = inputs_function(num1,num2)
            print(floor_division(num1, num2))
        elif operation=="%":
            num1, num2 = inputs_function(num1,num2)
            print(modulo(num1, num2))
        elif operation=="**":
            num1, num2 = inputs_function(num1,num2)
            print(exponentiation(num1, num2))
        elif operation=="sqr":
            num=float(input("Enter one number: "))
            print(square_root(num))
        elif operation=="gcd":
            num1, num2 = inputs_function(num1,num2)
            print(greatest_commun_divisor(num1,num2))
        ask=input("Do you want to calculate again? (y/n): ")
        if ask !="y":
            break
    except ValueError:
        print("That's not a valid number.")