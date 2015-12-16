import numpy as np
import random


dimension=10
#route = np.ones(dimension,dtype=int)

route = random.sample(range(dimension), dimension)


print(route[::-1])
print(route)
