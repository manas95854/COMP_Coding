name = input("Enter a name: ")

if name == name[::-1]:
    print("The name is a palindrome.")
else:
    print("The name is not a palindrome.")