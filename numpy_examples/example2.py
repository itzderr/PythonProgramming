import random
import numpy as np

# pure python
users = []

for i in range(5000):
    random_height = round(random.uniform(1.5, 2.0), 2)
    random_weight = round(random.uniform(40, 100), 2)
    random_user = [random_height, random_weight]
    users.append(random_user)

print(users)

# 1. mean and median of users' weight
# mean
# - get the list of only weights
weights = []
for user in users:
    weights.append(user[1])
# - get the sum of weights / the number of users
print(f"mean: {sum(weights) / len(weights)}")

# median
# - sort the list of weights
weights.sort()
# - get the middle value
print(f"median: {weights[len(weights) // 2]}")

# numpy
np_height = np.round(np.random.normal(1.70, 0.2, 5000), 2)
np_weight = np.round(np.random.normal(65, 15, 5000), 2)
np_users = np.column_stack((np_height, np_weight))
print(np_users)

# 2. mean and median of users' weight
print(np.mean(np_users[:, 1]))
print(np.median(np_users[:, 1]))


