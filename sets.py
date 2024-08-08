# ===> Set

cities = {'Islamabad', 'Lahore', 'Dehli', 'Mummbay'}

cities2 = {'London', 'Paris', 'New York','Islamabad', 'Lahore'}

set1 = {'apple', 'banana','mango',True,False, 0, 2,4.5, 9}

print(type(cities), cities)

print(type(set1), set1)

# ===> Access Items
for i in set1:
    print(i)

print('=============')

print('banana' in set1)

print(3 not in set1)

# ===> Add item

cities.add('Kabul')
print(cities)

afghanCities = {'Kabul', 'Nagrahar'}
print(type(afghanCities),afghanCities)
cities.update(afghanCities)
print(cities)

# ===> Add Any Iterable

pakCities = ['Peshawar','Karachi']
print(type(pakCities),pakCities)

cities.update(pakCities)
print(cities)

tuple1 = ('Paktiya',)
print(type(tuple1),tuple1)

cities.update(tuple1)
print(cities)

# ===> Remove Item

cities.remove('Paktiya')
print(cities)

cities.discard('Mummbay')
print(cities)

cities.pop()
print(cities)

afghanCities.clear()
print(afghanCities)

del pakCities
# print(pakCities)

# ===> Loop Items
for city in cities2:
    print(city)

# ===> Join Sets

# Union of two sets
print(type(cities),cities)
print(type(cities2),cities2)
citiesUnion =  cities.union(cities2)
print(type(citiesUnion),citiesUnion)

citiesUnion2 =  cities | cities2
print(type(citiesUnion2),citiesUnion2)


# Intersection of two sets

citiesIntersection1 = cities.intersection(cities2)
print(citiesIntersection1)

citiesIntersection2 = cities & (cities2)
print(citiesIntersection2)

# cities.intersection_update(cities2)
# print(cities)

# Difference
difference1= cities.difference(cities2)
print(difference1)

difference2 = cities - cities2
print(difference2)

# cities.difference_update(cities2)
# print(cities)

# ===> Symmetric Differences

sDifference1 = cities.symmetric_difference(cities2)
print(sDifference1)

cities.symmetric_difference_update(cities2)

print(cities)