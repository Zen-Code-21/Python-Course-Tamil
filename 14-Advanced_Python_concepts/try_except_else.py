
a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
try:
    print(f"the sum is {a / b}") 

except Exception as e:
    print(e)

#only excecutes if there is no error in the try block
else:
    print("Hey i am good")
