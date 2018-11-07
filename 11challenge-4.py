##Make a Hexaogon class with a method called calculate_perimeter that calculates and returns its
##perimeter. Then create a Hexagon object, call calculate_perimeter on it, and print the results.

##class Hexagon():
##    def __init__(self, a):
##        self.side = a
##        print("Object Created")
##
##    def calculate_perimeter(self):
##        return self.side * 6
##    
##hexagon = Hexagon(32)
##print("Side: ", hexagon.side)
##print("Hexagon perimeter = ", hexagon.calculate_perimeter())

##Instructor's solution assumes a hexagon with unequal sides

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        
    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6
    
a_hexagon = Hexagon(11, 22, 33, 44, 55, 66)
print(a_hexagon.calculate_perimeter())
    
    
