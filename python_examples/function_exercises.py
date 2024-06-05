# 1
def greet(name: str):
    print(f"Hello, {name}!")

# greet("Derrick")


# 2
def square(n: int) -> int:
    return n ** 2


# 3
def add(a: int, b: int) -> int:
    return a + b


# 4
def greet_user(name: str = "Guest"):
    print(f"Welcome, {name}!")


# greet_user("Derrick")

# 5
def format_address(street: str, city: str, country: str) -> str:
    return f"{street}, {city}, {country}"


# print(format_address("68 Smithe ST", "Vancouver", "Canada"))

# 6
def factorial(n: int) -> int:
    """
    Returns the factorial of the given integer n.
    :param n: integer
    :return: the factorial of the given integer n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


# 7
def calc_bmi(height: float, weight: float) -> float:
    """
    returns the bmi from the given height and weight
    :param height: height in meter as float
    :param weight: weight in kg as float
    :return:
    """
    return weight / (height * height)


# print(calc_bmi(1.78, 75))


# 8
def multiply(a, b):
    return a * b


# print(multiply(10, 20))

# 9
def reverse_string(s: str) -> str:
    return s[::-1]


# 10
def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


# print(is_even(10))
# print(is_even(9))

# 11
def sum_list(l: list) -> int:
    return sum(l)


# 12
def count_vowels(s: str) -> int:
    count = 0
    for ch in s:
        if ch in "AEIOUaeiou":
            count += 1

    return count


# print(count_vowels("abcde"))

# 13
def find_max(a: int, b: int, c: int) -> int:
    # max(a, b, c)
    if a > b > c or a > c > b:
        return a
    elif b > a > c or b > c > a:
        return b
    else:
        return c


# 14
def is_palindrome(s: str) -> bool:
    last = len(s) // 2
    for i in range(last):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True


# 15
def celsius_to_fahrenheit(c: float) -> float:
    return c * 1.8 + 32


# print(celsius_to_fahrenheit(30))

