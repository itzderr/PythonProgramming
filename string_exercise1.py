# 1
message = "Hello, World!"
print(message[0])
print(message[len(message) - 1])

# 2
s1 = "Python Programming"
space = s1.find(" ")
print(s1[0:space])
print(s1[space + 1:])

# 3
print(message.upper())
print(message.replace("World", "Python"))

# 4
print("Hello" + " " + "World")

# 5
fruits = "apple,banana,cherry"
print(fruits.split(","))

# 6
name = "Leo"
age = 6

# newer
formatted_string = f"My name is {name} and I am {age} years old"

# older
formatted_string2 = "My name is {} and I am {} years {}".format(name, age, "old")

print(formatted_string)

# 7
user_string = input("Enter a string: ")
print(user_string[::-1])



