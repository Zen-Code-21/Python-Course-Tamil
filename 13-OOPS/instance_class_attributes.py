
class Employee:

    company = "Cognizant" #This is a class attribute
    
    def __init__(self, salary, name, bond, company):

        self.salary = salary  #create an instance attribute and assign it to the parameter "salary"
        self.name = name    
        self.bond = bond
        self.company = company #This is an instance attribute

a = Employee(10000, "Alex", 3, "TCS")      
# print(a.company)   #always prints the instance attribute if it is present
# print(Employee.company) #This will always print the class attribute


#Object introspection:   #This command is used to list out all the attributes and methods of an object
print(dir(a))             
