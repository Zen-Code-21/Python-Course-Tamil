
class Employee:
    company = "HP" #this is a class attribute
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary #this is a instance attribute

    #this is an instance method(this is default)
    def get_info(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

    #these are static methods in python
    @staticmethod
    def sum(a,b):
        return a + b
    
    
    
    # these are class methods in python
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

e1 = Employee("John", 30000)
e2 = Employee("Jack", 50000)

# e1.get_info()
# e2.get_info()
# print(e1.sum(2,4))
print(Employee.company)
e2.change_company("TCS")
print(Employee.company)


