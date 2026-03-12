mylist = [2,5,8,4,6,2,5]
even = 0
odd = 0
for i in mylist:
    if i%2==0:
        even += 1
    else:
        odd += 1
print("even = ", even)
print("odd = ", odd)