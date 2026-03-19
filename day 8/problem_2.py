# nested function

def outerFuction():
    print("This is my outer function") # second execute
    def innerFunction(): 
        print("Inner function")
    innerFunction() # thied execute
outerFuction() # first execute start from her