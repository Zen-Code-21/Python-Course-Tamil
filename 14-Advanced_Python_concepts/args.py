# here args is a tuple that takes n number of variable arguments in the sum function
def sum(*args):
    total = 0
    for item in args:
        total += item
    return total

print(sum(300,2,3))