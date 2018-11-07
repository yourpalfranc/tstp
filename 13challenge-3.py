##Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape"
##when called. Change your Square and Rectangle classes from the previous challenges to inherit
##from Shape, create Square and Rectangle objects, and call the new method on both of them.

class Shape:
    def __init__(self, my_shape):
        self.my_shape = my_shape
        
    def what_am_i(self):
##        print_shape = str(self.my_shape)
##        print("I am a", str(self.my_shape))
        print("I am a", self.my_shape)
        
class Rectangle(Shape):
    pass
    
class Square(Shape):
    pass


rectangle_print = Rectangle("rectangle")
square_print = Square("square")
print(rectangle_print.what_am_i())
print(square_print.what_am_i())
##my_print = Shape("square")
##print(my_print.what_am_i())

