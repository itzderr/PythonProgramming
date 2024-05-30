# function
# - built-in: print, max, sum, min, round, ...
# - "reusable block of code"

# cm, kg
heights = [178.81, 162.56, 193.26, 165.72, 170.27]
# search function to round up to 1 decimal point
heights_updated = []

for height in heights:
    heights_updated.append(round(height, 1))

print(heights_updated)

# - user defined functions (your own custom function)
#   (DocString)

def factorial(n: int) -> int:  # function header (prototype)
    """
    Returns the factorial of the given integer n.

    :param n: an integer
    :return: the factorial of the given integer n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i  # result = result * i
    return result


x = factorial(5)
print(x)

