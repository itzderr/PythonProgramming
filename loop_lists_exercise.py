# 1
for i in [10, 20, 30, 40, 50]:
    print(i)

# 2
sum = 0
for i in [1, 2, 3, 4, 5]:
    sum += i

print(sum)

# 3
l = [3, 7, 2, 9, 4]
max = l[0]

for i in l:
    if i > max:
        max = i

print(max)

# 4
l = [1, 4, 4, 2, 4, 3]
count = 0
for i in l:
    if i == 4:
        count += 1

print(count)

# 5
l = [1, 2, 3, 4, 5]
squared = []

for i in l:
    squared.append(i ** 2)

print(squared)

# 6
l = ["Python", "is", "awesome"]
result = ""
for i in l:
    result += i

print(result)

# 7
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_l = []

for i in l:
    if i % 2 == 0:
        even_l.append(i)

print(even_l)

# 8
l = [2, 4, 6, 8]
double_l = []
for i in l:
    double_l.append(i * 2)

print(double_l)

# 9
l = [1, 3, 3, 4, 3, 5, 3]
new_l = []
for i in l:
    if i != 3:
        new_l.append(i)

l = new_l
print(l)

# 10
l = [5, 7, 8, 7, 10]
for i in range(len(l)):
    if l[i] == 7:
        print(i)
        break

