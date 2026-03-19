# write a probem to perform arithmetic operations using functional programming approach 
# function help us to acheive modularity approach

import sys
def addition(num1,num2):  # called function
    print("Addition = ", num1 + num2)

def subtraction(num1,num2): # called function
    print("Subtraction = ", num1 - num2)

def multiplication(num1,num2): # called function
    print("Multiplication = ", num1 * num2)

def division(num1,num2): # called function
    print("Division = ", num1 / num2)

while True:
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Exit ")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        sys.exit()
    val1 = int(input("Enter first value : "))
    val2 = int(input("Enter second value : "))  
    if choice == 1:
        addition(val1, val2)
    elif choice == 2:
        subtraction(val1, val2)
    elif choice == 3:
        multiplication(val1, val2)
    elif choice == 4:
        division(val1, val2)
    else:
        print("Your are enter invalid choice ")
    
    