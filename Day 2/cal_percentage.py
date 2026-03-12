m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

print("Total marks:", total)
print(f"Percentage: {percentage:.2f}%")


if percentage >= 60:
    print("Eligible for placement")
else:
    print("Not eligible for placement")
