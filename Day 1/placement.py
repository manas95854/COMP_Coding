p1 = float(input("Enter marks for paper 1: "))
p2 = float(input("Enter marks for paper 2: "))
p3 = float(input("Enter marks for paper 3: "))

total = p1 + p2 + p3
per = total / 3

print("Total Marks:", total)
print("Percentage:", per)

if per >= 60:
    print("Eligible for placement")
else:
    print("Not eligible")
