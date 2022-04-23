# define a function `call` where you provide the function and the arguments
def call(x, f):
    return f(x)

# define a function that returns the square
square = lambda x : x*x

# define a function that returns the increment
increment = lambda x : x+1

# define a function that returns the cube
cube = lambda x : x*x*x

# define a function that returns the decrement
decrement = lambda x : x-1

# put all the functions in a list in the order that you want to execute them
funcs = [square, increment, cube, decrement]

# bring it all together. Below is the non functional part. 
# in functional programming you separate the functional and the non functional parts.
from functools import reduce # reduce is in the functools library
print(reduce(call, funcs, 96)) # output 783012621312