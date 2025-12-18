
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def sum(self,p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"The value of X is {self.x} and the value of Y is {self.y}")

    def __add__(self, p):
         return Point((self.x + p.x), (self.y + p.y))
    

#(2,5)
#(3,4)
#The sum of the above 2 points is (5,9)

p1 = Point(2,5)
p2 = Point(3,4)

# p = p1.sum(p2)
p = p1 + p2
p.print_point()




