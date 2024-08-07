fruits = ('apple', 'mango', 'orange', 'banana')

print(type(fruits),fruits)
print(len(fruits))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(type(tuple4),tuple4)

# ====> Access Tuple Items

print(fruits[3])

# ===> Negative indexing

print(fruits[-2])

# ===> Range indexing
print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])

# ===> Check if Item Exists\

if 'mango' in fruits:
    print('Yes, Mango are present in tuple')
else:
    print('No, Mango are not present in tuple')

# ===>Change Tuple Values

tem = list(fruits)

tem.append('melon')
print(type(tem),tem)
fruits = tuple(tem)
print(type(fruits),fruits)

# ===> Add tuple to a tuple

tempFruits = ('cherry',)

fruits += tempFruits
print(fruits)

# ===> Remove Items
temp = list(fruits)
temp.remove('melon')

fruits = tuple(temp)
print(fruits)

# ===> Unpacking a Tuple
(v,w,x,y,z) = fruits
print(v)
print(w)
print(x)
print(y)
print(z)

# ===> Using Asterisk*
(x,y,*z) = fruits
print(x)
print(y)
print(z)

(x,*y,z) = fruits
print(x)
print(y)
print(z)

# ===> Loop Through a Tuple

for i in fruits:
    print(i)

for i in range(len(fruits)):
    print(fruits[i])

i = 0
while (i<len(fruits)):
    print(fruits[i])
    i +=1

# ===> Join Two Tuples

joinTuple = tuple1 + tuple2

print(tuple1)
print(tuple2)
print(joinTuple)

newTuple = fruits * 2
print(newTuple)