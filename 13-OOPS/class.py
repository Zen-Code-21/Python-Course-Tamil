#class : a blueprint or template. eg: form contains details like student name, age, course, father's name, mother's name 

#object : Specific instance or entity that is created from the class. A student named John is filling the form and that will be considered as an object of the class

class Employee_of_IBM:
    company = "IBM"

    def get_salary(self):
        print(self)
        return 40000
    
class Employee_of_Accenture:
    company = "Accenture"

    def get_salary(self): #You need to include self as the first parameter in every instance method because Python uses it as the reference to the object on which the method is called.
        print(self)
        return 45000

e1 = Employee_of_IBM()
print("The company of e1 is :", e1.company)
print("salary of e1:", e1.get_salary())

e2 = Employee_of_Accenture()
print("The company of e2 is:", e2.company)
print("salary of e2:", e2.get_salary())
    


