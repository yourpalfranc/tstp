##Create a Circle class with a method called area that calculates and returns its area. Then create
##a circle object, call area on it, and print the result. Use Pythons pi function in the built-in
##math module.
import math

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius**2)


circle = Circle(5)
print(circle.area())

##class Rectangle():
##    def __init__(self, w, l):
##        self.width = w
##        self.len = l
##        
##    def area(self):
##        return self.width * self.len
##    
##rectangle = Rectangle(10, 20)
##print(rectangle.area())