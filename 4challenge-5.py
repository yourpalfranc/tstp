#Challenge 5: write a function that converts a string to a float and returns the result. Use
#exception handling to catch the exception that could occur.
def string_to_float(x):
    return float(x)

try:
    print(string_to_float(one))
except NameError:
    print("cannot be a character or string")



#HAVEN'T COVERED EXCEPTION HANDLING YET

#example from Exception Handling video
#a = input("type a numbr:")
#b = input("type another:")
#a = int(a)
#b = int(b)

#try:
#   print(a/b)
#except ZeroDivisionError:
#    print("b cannot be zero")
