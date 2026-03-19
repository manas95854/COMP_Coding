#write a program to calculate and return the sum of distance between adjacent number in an array of positive number


mylist = []
sum = 0
N = int(input("Enter the number of elements in the array: "))
for i in range(N):
    val = int(input("Enter the element: "))
    mylist.append(val)


for j in range(len(mylist)):
    if j+1 in range(len(mylist)):
        sum += abs(mylist[j] - mylist[j+1])


print("The sum of distance between adjacent number in the array is: ", sum)