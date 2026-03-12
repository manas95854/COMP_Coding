num1 = int(input("Enter no 1: "))
num2 = int(input("Enter no 2: "))
num3 = int(input("Enter no 3: "))

if num1 > num2:
    if num1 > num3:
        print("Maximum value is:", num1)
    else:
        print("Maximum value is:", num3)
else:
    if num2 > num3:
        print("Maximum value is:", num2)
    else:
        print("Maximum value is:", num3)