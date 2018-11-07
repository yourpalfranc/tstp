#Challenge 4: write a program with two functions. The first function should take an integer as a
#parameter and return the result of the ingeger divided by 2. The second function should take
#an integer as a parameter an return the result of the integer multiplied by 4. Call the first
#function, save the result as a variable, and pass it as a parameter to the second function.
def divide(x):
    return x / 2

def mult(y):
    return y * 4

result = divide(mult(4))
print(result)

#solution
def divide(x):
    return x / 2

def multiply(x):
    return x * 4

y = divide(4)
z = multiply(y)
print(z)
