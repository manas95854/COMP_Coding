def searchValue(mylist):
    sum =0
    for i in range(len(mylist)):
        sum = sum + mylist[i]
    return sum
mylist = [1,2,3,4,5,6]
res = searchValue(mylist)
print("Sum of array = ",res)