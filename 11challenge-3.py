##Create a Triangle class with a method called area that calculates and returns its area. Then create
##a triangle object, call area on it, and print the result. Use Pythons pi function in the built-in
##math module.

import math

class Triangle():
    def __init__(self, sidea, sideb, sidec):
        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec
        print("Object Created")

    def half_perimeter(self):
        return (self.sidea + self.sideb + self.sidec)/2
    
    def area(self):
##        p = triangle.half_perimeter()
##        aminus = self.sidea
##        bminus = self.sideb
##        cminus = self.sidec
        return math.sqrt(triangle.half_perimeter() * ((triangle.half_perimeter() - self.sidea) * (triangle.half_perimeter() - self.sideb) * (triangle.half_perimeter() - self.sidec)))

triangle = Triangle(24, 30, 18)
##print(triangle.half_perimeter())
print("Side A: ", triangle.sidea)
print("Side B: ", triangle.sideb)
print("Side C: ", triangle.sidec)
print("Area = ", triangle.area())
