class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @property
    def second_name(self):
        l = self.name.split(" ")
        print(l)
        return l[1]

    @second_name.setter    
    def second_name(self,second_name):
        l = self.name.split(" ")
        new_name = f"{l[0]} {second_name}"
        self.name = new_name
    
e = Employee("John Doe", 45000)

print(e.second_name)
e.second_name = "Wick"
print(e.name)

# e.projects = 6
# print(e.projects)
# print(e.first_name())
# e.set_second_name("Wick")
# print(e.name)

