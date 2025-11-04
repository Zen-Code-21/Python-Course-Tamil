def add(a,b):
    #the variables declared inside any block are called local variables
    c = a + b
    z = 1 #this will create a new local variable that will get destroyed when the function returns
    return c

def hello():
    z = 45
    print("hello everyone")


z = 30 #this is a global variable and it can be accessed anywhere in the program
print(add(2,3))
hello()
print(z)