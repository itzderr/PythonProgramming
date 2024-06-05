# 1. Palindrome
def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")


is_palindrome("madam")
is_palindrome("hello")


# 2. list to string conversion
l = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(l))