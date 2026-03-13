mydict = {
    101: "Manas",
    102: "Rohit",
    103: "Sita",
    104: "Gita",
    101: "Manas "
}
print(mydict)

#only print value of key 102
a = mydict[102]
print(a)

#overwrite value of key 102
mydict[102] = "peter"
print(mydict)

#only print keys
for x in mydict:
    print(x)

# only print values
for x in mydict.values():
    print(x)

#printing both keys and values
for x,y in mydict.items():
    print(x,y)

#if i have to ad new key value pair in dictionary
mydict["mobile number"] = 1234567890
print(mydict)

#if i have to delete a key value pair from dictionary
mydict.pop(101)
print(mydict)