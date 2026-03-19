# removing space from the string
#1. rstrip() - removes space from the right end of the string
#2. lstrip() - removes space from the left end of the string
#3. strip() - removes space from both ends of the string

city = input("Enter the name of the city: ")
scity = city.strip()
if scity == "Bangalore":
    print("Welcome to Bangalore")
elif scity == "Mysore":
    print("Welcome to Mysore")
elif scity == "Hubli":
    print("Welcome to Hubli")
else:
    print("your entered city is not in our database")