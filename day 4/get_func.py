n = int(input("enter the number of student:"))
d = {}
for i in range(n):
    name = input("enter student name:")
    marks = int(input("enter student marks:"))
    d[name] = marks

while True:
    name = input("enter student name to get marks: ")
    marks = d.get(name,-1)
    if marks == -1:
        print("student not found")
    else:
        print("the marks of",name,"is",marks)
    option =input("do you want to fid another student marks? (yes/no): ")
    if option=="no":
        break

print("thank you for using the application")