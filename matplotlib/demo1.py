import matplotlib.pyplot as plt
import numpy as np

year = np.sort(np.random.randint(1950, 2050, 1000))
pop = np.sort(np.random.normal(5, 1.5, 1000))

plt.scatter(year, pop)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")

plt.show()