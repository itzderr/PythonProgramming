# Loops: for-loop, while-loop
# - to repeat a block of code

# syntax (structure)
# for each_element(var) in iterables(collections):
#     code to repeat

# 1. iterate a range of numbers
# To get the sum even numbers from 1 to 10
sum = 0
for i in range(1, 11):
    if i % 2 == 0:  # %: remainder
        sum += i  # sum = sum + i

print(sum)

# 2. iterate a sequence of characters (string)
city = "Vancouver"
count_vowels = 0
for ch in city:
    if ch in "AEIOUaeiou":
        count_vowels += 1

print(f"The number vowels in {city} is {count_vowels}.")


# 3. iterate a sequence of any data elements (list)
provinces = ["AB", "BC", "ON", "QB", "SK", "PR"]
for province in provinces:
    if province in ["AB", "BC", "ON", "SK"]:
        print(f"{province} speaks English")
    elif province == "QB" or province == "PR":  # province in ["QB", "PR"]
        print(f"{province} speaks French")

# 'break' to stop the loop



