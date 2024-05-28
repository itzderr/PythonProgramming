# list - a sequence of elements
cities = ["Ottawa", "Brasilia", "Mexico City", "Tokyo", "Seoul", "La Paz"]

for city in cities:
    print("Hello, " + city)

# index
print(cities[0])  # first
print(cities[len(cities) - 1])  # last

# slice (sublist)
print(cities[0:3])

# reverse a list
print(cities[::-1])

# list methods
# 1. append(item): add the item at the end of the list
cities.append("Washington DC")
print(cities)

# 2. pop(index): remove the item at the given index
cities.pop(0)
print(cities)

# 3. index(item): returns the index of the given item in the list
print(cities.index("Tokyo"))

# nested list (list of lists)
info = [["Vancouver", "Burnaby"], ["Calgary", "Edmonton"], ["Toronto", "Ottawa"]]
print(info[0][0])  # first element of the first list in the nested list




