# here, kargs is a dictionary that takes n number of key - value pair arguments in the marks function
def marks(**kwargs):
    print(kwargs)

marks(john = 40, doron = 90, alex = 87, ronaldo = 91, nancy = 75)