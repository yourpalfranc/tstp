##Add a square_list class variable to a class called Square to that every time you create a new
##Square object, the new object gets added to the list.
class Square():
    square_list = []
    
    def __init__(self, sides):
        self.side_length = sides
        self.square_list.append(self.side_length)
        
s1 = Square(20)
s2 = Square(30)
s3 = Square(40)
s4 = Square(50)

print(Square.square_list)