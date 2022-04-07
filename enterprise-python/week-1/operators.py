from operator import *
var1 = 2
var2 = 3
print('number var1= {}'.format(var1))
print('number var2 = {}'.format(var2))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(var1, var2): {}'.format(func.__name__, func(var1, var2)))