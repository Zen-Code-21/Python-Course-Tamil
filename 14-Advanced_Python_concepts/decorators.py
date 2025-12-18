
def decorator(func):
    def wrapper():
        print("I am going to execute this function...")
        func() #the content inside say_hello will be excecuted here
        print("I have excecuted this function")
    return wrapper


@decorator
def say_hello():
    print("Hello there !")

say_hello()

# f = decorator(say_hello)
# f()