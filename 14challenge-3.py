##Write a function that takes two objects as perameters and returns True if they are the same
##object and False if not

##class Dog():
##    pass
##
##class Cat():
##    pass
##
##a = Dog()
##b = Dog()
##c = Cat()
##
##def compare_animals(a1, b1):
##    print(a1, " .vs ", b1)
##    if a == b:
##        return True
##    else:
##        return False
##    
##print(compare_animals(a, c))

##instructor solution
def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "a"))
    