def msg():#calling function
    val1=int(input("enter first number"))
    val2=int(input("enter first number"))
    sum=val1+val2
    mul=val1*val2
    div=val1/val2   
    sub=val1-val2
    return sum,mul,div,sub
    #return val1+val2    
res =msg()
print("Result:", res)