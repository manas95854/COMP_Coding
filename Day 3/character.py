char = ord(input("Enter a character: "))
if char>=65 and char<=91:
    print("The entered character is in upper case.")
elif char>=97 and char<=122:
    print("The entered character is in lower case.")
elif char>=48 and char<=57:
    print("The entered character is a digit.")
else:
    print("The entered character is a special character.")
