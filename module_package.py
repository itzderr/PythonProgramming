# "we want to use other people's code"

# module = a python file
# package = many modules; folder, directory
# library = many packages

import function_exercises as f
from random import randint
import numpy as np

# print(f.celsius_to_fahrenheit(30))
# x = randint(1, 20)
# print(x)
heights = [1.78, 1.65, 1.50, 1.80, 1.95]
weights = [75, 55, 50, 92, 101]

# 1. pure python version
# bmis = []
# for i in range(len(heights)):
#     bmis.append(round(weights[i] / heights[i] ** 2, 2))
# print(bmis)

# 2. numpy version
np_heights = np.array(heights)
np_weights = np.array(weights)
np_bmis = np_weights / np_heights ** 2

print(np_bmis)
