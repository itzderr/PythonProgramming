# 1
nums = [1, 2, 3, 4, 5]
print(nums[2])

# 2
nums.append(6)
print(nums)
nums.pop(1)
print(nums)

# 3
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(values[:5])
print(values[len(values)-3:])
print(values[::2])

# 4
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(nums))
print(max(nums))
print(min(nums))

# 5
l = [i * i for i in range(1, 11)]
print(l)

# 6
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested[1][1])

