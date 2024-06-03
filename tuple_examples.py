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
# t[0] = 0   error!
print(type(t))
print(t)
print(t[0] + t[1])

