
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name of the person is {self.name} and the age is {self.age}"
    
    def __repr__(self):
        return f"name = {self.name} \n age = {self.age}"
    
    def __len__(self):
        return len(self.name)
    
    

p1 = Person("Will" , 30)
# print(p1.name)
# print(p1.age)
# print(repr(p1))
print(len(p1))