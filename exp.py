import numpy as np
import math
import random
#import TSP
import timeit

N = 100
b = np.random.random_integers(50, 100, size=(N, N))

data = (b + b.T)/2

print(TSP.NearestNeighbor(data).solve())

#print(TSP.SMA(data, inittemp=1000, finaltemp=1, equilibrium=100, cooling='logaritmic',coolingparam=0.7, neighbor='2opt').solve())


print(random.sample(range(10), 10))


start_time = timeit.default_timer()
for i in range(100000):
   len(data[0])
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
for i in range(100000):
    data.shape[0]
print(timeit.default_timer() - start_time)