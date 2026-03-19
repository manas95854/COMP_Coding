# input = manas is good programmer
#WAP yo count the word
# output = 4

name = "manas is good programmer"
count = 1
for i in name:
    if i == " ":
        count += 1
    else:
        continue
print("Total word in string is : ", count)