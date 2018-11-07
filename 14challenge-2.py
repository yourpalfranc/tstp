##Change the Square class so that when you print a square object, a message prints telling you the
##len of each of the four sides of the shape. For example, if you ceate a square with Square(29)
##and print it, Python should print 29 by 29 by 29 by 29.

class Square():
    square_list = []
    
    def __init__(self, sides):
        self.side_length = sides
        self.square_list.append(self.side_length)
        
    def print_sides(self):
        print(self.side_length, " by ", self.side_length, " by ", self.side_length, " by ", self.side_length)
        
s1 = Square(29)
s2 = Square(30)
s3 = Square(40)
s4 = Square(50)

##print(s1.side_length)
s1.print_sides()