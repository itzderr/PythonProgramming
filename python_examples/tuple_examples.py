# int, float, bool, str
# list - a sequence of any elements
# tuple - "immutable comma separated values"

l = [1, 2, 3, 4, 5]
l[0] = 0
print(type(l))
print(l)

t = (1, 2, 3, 4, 5)
# t.index(3)
# t.count(3)
# t[0] = 0  # error!
print(type(t))
print(t)
print(t[0] + t[1])


# example 1 : when you have a set of immutable data
seat_types = ("Window", "Aisle")
user_seat = input("Select your seat type (Window, Aisle): ")

if user_seat in seat_types:
    print("Thank you")
else:
    print("Wrong seat type")


# example 2 : multiple meaningful values
user1 = ("Jenny", 25, "BC")
name, age, prov = user1

print(name)
print(age)
print(prov)

# boolean operator examples
s = "abc"
if not len(s) <= 3:  # len(s) > 3
    print("hello")

