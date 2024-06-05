
employees = {"D1": ["John", 2020, "Canadian"],
             "U2": ["David", 2021, "American"],
             "H3": ["Wendy", 2019, "Mexican"]}

# print(type(employees))

emp1 = employees["D1"]
# print(emp1[0])
# print(emp1[1])
# print(emp1[2])

# 1. iterating key, value pairs
for (k, v) in employees.items():
    print(k, v)

# 2. iterating by key
for k in employees.keys():
    print(k)

# 3. iterating by value
for v in employees.values():
    print(v)

# 4. add new data entry (key-value pair)
employees["M4"] = ["Jenny", 2015, "Indian"]
employees["F5"] = ["Matt", 2017, "Canadian"]

print(employees)

# 5. remove an entry
del employees["M4"]

print(employees)

# 6. update an entry
employees["F5"] = ["Matthew", 2017, "Canadian"]

print(employees)

# examples
# 1. get the list of names
names = []
for k, v in employees.items():
    names.append(v[0])

print(names)

# 2. get the average year employees joined the company
years_joined = []
for k, v in employees.items():
    years_joined.append(v[1])

print(sum(years_joined) / len(years_joined))
