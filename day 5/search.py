mylist = [4,2,7,8,5,4,1]
def searchValue(target):
    for i in range(len(mylist)):#len =7
        if mylist[i] == target:
            return i
        
    return -1
target = 15
res = searchValue(target) #calling function
if res != -1:
    print("value found at index number = ", res)

else:
    print("value not found")