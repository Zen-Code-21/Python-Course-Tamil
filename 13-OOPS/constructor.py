
class Employee:
    
    def __init__(self, salary, name, bond):

        self.salary = salary  #create an instance attribute and assign it to the parameter "salary"
        self.name = name
        self.bond = bond
        
    def get_salary(self):
        return self.salary
    
    def get_info_of_employee(self):
        print(f"The name of the employee is {self.name}, and the salary is {self.salary} and the bond they are going to serve in this company is {self.bond} years")
    
e = Employee(45000, "John wick", 2)
# print(e.get_salary())
e.get_info_of_employee()

    