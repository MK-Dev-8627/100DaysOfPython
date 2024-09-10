# Map

numbers = [1,2,3,4,5,6,7,8,9]
print(f'Numbers: {numbers}')
def squareFunc(x):
    return x*x

squares = list(map(squareFunc, numbers))
print(f'Squares: {squares}')

cubes = map(lambda x: x*x*x, numbers)
print(f'Cubes: {list(cubes)}')

# Filters

def filterFunc(x):
    return x>5

filtersNum = filter(filterFunc,numbers)

print(f'Filters Numbers: {list(filtersNum)}')

smallNum = filter(lambda x: x<6, numbers)

print(f'Small Numbers: {list(smallNum)}')

# reduce 
from functools import reduce 

def sum(a, b):
    return a + b

total = reduce(sum, numbers)
print(f'Sum of Numbers: {total}')

multiply = reduce(lambda a,b: a*b, numbers)

print(f'Multiplication of Numbers: {multiply}')


