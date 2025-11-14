
a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b)) #contains all the elements in a along with all the elements in b

c = a.intersection(b) #contains only the elements that are present in a as well as b
print(c)

print(a.difference(b))  #subtracts set b from set a 