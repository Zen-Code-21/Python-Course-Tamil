def add(a,b):
    #the variables declared inside any block are called local variables
    c = a + b
    global z  #go ahead and access the global variable z
    z = 10 
    return c

z = 30
print(add(5,4))
print(z)