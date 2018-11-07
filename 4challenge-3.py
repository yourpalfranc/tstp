#Challenge 3: write a function that takes three required parameters and two optional parameters
#def my_function(a,b,c,d=1,e=2):

#solution
def add_mult(a,b,c,x=100,y=1000):
    return a + b + c * x * y

result = add_mult(10,15,25)
print(result)


