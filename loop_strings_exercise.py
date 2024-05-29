# 1
for ch in "Python":
    print(ch)

# 2
count = 0
for ch in "data science":
    if ch in "aeiouAEIOU":
        count += 1

print(count)

# 3
s = "hello world"
i = len(s) - 1
reversed_s = ""

while i >= 0:
    reversed_s += s[i]
    i -= 1  # i = i - 1

print(reversed_s)

# 4
s = "coding"
for ch in s:
    print(ord(ch))

# 5
count = 0
for ch in "experience":
    if ch == "e":
        count += 1

print(count)

# 6
s = "education"
result = ""

for ch in s:
    if ch in "aeiouAEIOU":
        result += "*"
    else:
        result += ch  # result = result + ch

print(result)

# 7
s = "looping"
result = ""
for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]

print(result)

# 8
s = "swiss"
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for ch in s:
    i = ord(ch) - ord("a")
    if l[i] == 1:
        print(ch)
        break
    else:  # l[i] == 0
        l[i] = 1

# 9
s = "machine learning is fun"
l = s.split(" ")
result = ""

for word in l:
    result += word.capitalize() + " "

print(result)

# 10
s = "racecap"
last = len(s) // 2
is_palindrome = True

for i in range(last):
    if s[i] != s[len(s) - 1 - i]:
        print("it is not a palindrome")
        is_palindrome = False
        break

if is_palindrome:
    print("it is a palindrome")