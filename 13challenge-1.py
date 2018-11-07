##Create Rectangle and Square classes with a method called calculate_perimeter that calculates
##the perimeter of the shape they represent. Create rectangle and square objects and call the 
##method on both of them

class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
        print("Object Created")

    def calculate_perimeter(self):
        return (self.width + self.length)*2
    
class Square(Rectangle):
    pass

my_rectangle = Rectangle(24, 30)
my_square = Square(10, 10)
print("Rectangle perimeter: ", my_rectangle.calculate_perimeter())
print("Square perimeter: ", my_square.calculate_perimeter())
