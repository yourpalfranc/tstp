##Define a method in your Square class called change_size that allows you to pass in a number
##that increases or decreases (if the number is negative) each side of a Square object by that 
##number.

class Shape(): 
    def what_am_i(self):
        print("I am a shape")
        
class Rectangle(Shape):
    def __init__(self, width, length,):
        self.width = width
        self.length = length
        print("Object Created")

    def calculate_perimeter(self):
        return (self.width + self.length)*2
    
class Square(Shape):
    def __init__(self, newnum):
        pass
    
    def change_size(self, newnum):
        if newnum >= 0:
            print("New Square perimeter: ", my_square.calculate_perimeter() + (newnum * 4))
        else:
            print("New Square perimeter: ", my_square.calculate_perimeter() + (newnum * 4))
        

my_rectangle = Rectangle(24, 30)
my_square = Square(10, 10)
print("Rectangle perimeter: ", my_rectangle.calculate_perimeter())
print("Square perimeter: ", my_square.calculate_perimeter())
my_square.change_size(2)
##rectangle_print = Rectangle("rectangle")
##square_print = Square("square")
my_rectange.what_am_i()
my_square.what_am_i()