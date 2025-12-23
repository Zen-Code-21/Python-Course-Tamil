def div(a, b):
    try:
        return a / b 

    except Exception as e:
        return e

    #this is always excecuted even if the try block completely excecutes or not
    finally:
        print("This is always excecuted...")


a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))

print(div(a,b))
