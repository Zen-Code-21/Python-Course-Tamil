
#recursion happens when a function calls itself

#fibonacci sequence:
# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6 7


'''
0 = 0
1 = 1
2 = fib(0) + fib(1)
3 = fib(1) + fib(2)
4 = fib(2) + fib(3)
5 = fib(3) + fib(4)
6 = fib(4) + fib(5)
n = fib(n - 2) + fib(n - 1)
'''

def fib(n): #in this case, n = 1
    #base case of recursion:
    if(n == 0 or n == 1):
        return n

    return fib(n - 2) + fib(n - 1)


# '''
#                        fib(6)
#               ___________/   \__________
#              /                           \
#           fib(4)                       fib(5)
#        ___/    \___                 ___/    \___
#       /            \               /            \
#    fib(2)         fib(3)        fib(3)         fib(4)
#    /   \          /    \        /    \         /    \
# fib(0) fib(1)  fib(1) fib(2)  fib(1) fib(2)  fib(2) fib(3)
#  0      1       1    /   \     1    /  \     /  \    /   \
#                      0    1          0  1   0    1  1     / \
#                                                 0         0   1 
# '''


print(fib(6))
'''
fib(4) +                                                   fib(5)
fib(2)+                   fib(3)                       + fib(3)              +              fib(4)    
fib(0) + fib(1)      +fib(1) + fib(2)               +fib(1)  +   fib(2)      +    fib(2)         +      fib(3)
0 + 1                +1         +fib(0) + fib(1)     +  1  + fib(0) + fib(1) +  fib(0) + fib(1)   +   fib(1)  +    fib(2)
0 + 1                +1          + 0   + 1           + 1   + 0   +    1      +   0     +  1       + 1         + fib(0) + fib(1)
0 + 1              + 1          + 0   +  1           + 1   + 0   +    1      +   0     + 1        + 1         +  0     +  1
'''



