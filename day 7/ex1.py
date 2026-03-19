#input = manas*is*a*good*programmer
#output = ****manasisagoodprogrammer
name = ' manas*is*a*good*programmer'
newname = ' '
val = ' ' 
for i in name:
    if i != '*':
        newname = newname + i
    else:
        val += i 

print(newname)
print(str(val + newname))