class Animal:

    location = "Europe"

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Genric Animal sound...")

class Dog(Animal): #This is how inheritance is done in python

    def speak(self):
        super().speak()
        print("Woof!")

d = Dog("Enzo")
# print(d.location)
d.speak()

# a = Animal("Lion")
# print(a.name)
# a.speak()