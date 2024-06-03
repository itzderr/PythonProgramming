import numpy as np
# python list
l = [1, 3.14, "Hello", True, [1, 2]]

# numpy array - only single data type
l1 = [1, 2, 3]
l2 = [1, 2, 3]

np_l1 = np.array(l1)
np_l2 = np.array(l2)

l3 = l1 + l2
np_l3 = np_l1 + np_l2

print(l3)
print(np_l3)

# python list
heights = [1.75, 1.82, 1.64, 1.70, 1.58]
weights = [69.4, 85.2, 54.3, 64.2, 50.8]
bmi = []
for i in range(len(heights)):
    bmi.append(weights[i] / heights[i] ** 2)

bmi_greater_than22 = []
for i in bmi:
    if i > 22:
        bmi_greater_than22.append(i)

print(bmi_greater_than22)

# numpy array
np_heights = np.array(heights)
np_weights = np.array(weights)
np_bmi = np_weights / np_heights ** 2

print(np_bmi)
print(np_bmi > 23)
print(np_bmi[1])
print(np_bmi[np_bmi > 22])

np_2d = np.array([[1.75, 1.82, 1.64, 1.70, 1.58],
                  [69.4, 85.2, 54.3, 64.2, 50.8]])
print(np_2d.shape)

# 1. get the first 3 people's heights and weights
print(np_2d[:, :3])
# 2. get the last 3 people's heights and weights
print(np_2d[:, 2:])

