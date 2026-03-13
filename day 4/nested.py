#print 1 1 1
#      2 2 2 
#     3 3 3

for i in range(1,4): #outer loop for rows
    for j in range(1,4):#inner loop for columns
        print(i,end=" ")
    print()


n = int(input("Enter a number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()


n = int(input("Enter a number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()

n = int(input("Enter a number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()