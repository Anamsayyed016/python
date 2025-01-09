#high order function

#map
# my_list=[10,20,30,40,50]
# def dec(x):
#     return x*5
# x=map(dec,my_list)
# print(list(x))

#filter

# my_tuple=( 70,75,60,59,60,80)
# def greater_60(x):
#     if x>60:
#         return x
# x=(filter(greater_60,my_tuple))
# print(list(x))

#reduce

# import functools.reduce
# from functools import reduce
# my_tuple=(10,20,30,60,50,40)
# def max_digit(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=reduce(max_digit,my_tuple)
# print(x)

from functools import reduce
my_tuple=('a','b','c','d','e','f')
def max_digit(x,y):
    if x>y:
        return x
    else:
        return y
x=reduce(max_digit,my_tuple)
print(x)
