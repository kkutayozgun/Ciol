import numpy as np
import  random
import timeit



def swap(rt, f, s):
  temp = rt[f]
  rt[f] = rt[s]
  rt[s] = temp
  return rt


#2-opt arc numbers starts from zero
def twoopt(rt, arc1, arc2):
  arc1 += 1
  while arc1 < arc2:
    rt = swap(rt, arc1, arc2)
    arc2 -= 1
    arc1 += 1
  return rt

#3-opt arc numbers starts from zero
def threeopt(rt, arc1, arc2, arc3):
    t1 = rt[arc3:]
    t1.append(rt[:arc1+1])
    t2 = rt[arc1+1:arc2+1]
    t3 = rt[arc2+1:arc3+1]
    n1 = list()
    n1.append(t1)
    n1.append(t3)
    n1.append(t2)
    n2 = list()
    n2.append(t1)
    n2.append(t3)
    n2.append(t2[::-1])
    n3 = list()
    n3.append(t1)
    n3.append(t2[::-1])
    n3.append(t3[::-1])
    n4 = list()
    n4.append(t1)
    n4.append(t3[::-1])
    n4.append(t2)
    return n1, n2, n3, n4

#iterative objective
def iterativeobj(distances, rt):
  obj = distances[rt[0]][rt[len(rt)-1]]
  for i in range(len(rt)-1):
    obj += distances[rt[i]][rt[i+1]]
  return obj

#incremental objective  for swap
def incrementalobj(distances,obj,rt,f,s):
    r = rt[:]
    r.append(rt[0])
    obj -= distances[r[f]][r[f+1]]
    obj -= distances[r[s]][r[s+1]]
    obj += distances[r[f]][r[s+1]]
    obj += distances[r[s]][r[f+1]]
    r.insert(0, r[len(r)-2])
    f += 1
    s += 1
    obj -= distances[r[f]][r[f-1]]
    obj -= distances[r[s]][r[s-1]]
    obj += distances[r[s]][r[f-1]]
    obj += distances[r[f]][r[s-1]]

    if f+1 == s or (f-1 == 0 and s == len(rt)):
        obj += 2*(distances[r[f]][r[s]])

    return obj

#incremental objective  for two-opt
def incrementaltwopt(distances,obj,rt,arc1,arc2):
    r = rt[:]
    r.append(rt[0])
    obj -= distances[r[arc1]][r[arc1+1]]
    obj -= distances[r[arc2]][r[arc2+1]]
    obj += distances[r[arc1]][r[arc2]]
    obj += distances[r[arc1+1]][r[arc2+1]]
    return obj




























N = 10
b = np.random.random_integers(50, 100, size=(N, N))

data = (b + b.T)/2
np.fill_diagonal(data, 0)


route = random.sample(range(N), N)
rnd = random.sample(range(N), 2)
rnd.sort()

print(data)
print(route)
print(rnd)

obj = iterativeobj(data, route)
print('Iterative obj:'+ str(obj))
"""
print('After Inceremental: '+str(incrementalobj(data, obj,route,rnd[0],rnd[1])))
print('After Swap Iterative: '+str(iterativeobj(data,swap(route,rnd[0],rnd [1]))))


start_time = timeit.default_timer()
for i in range(100000):
  incrementalobj(data, obj,route,rnd[0],rnd[1])
print(timeit.default_timer() - start_time)


start_time = timeit.default_timer()
for i in range(100000):
  iterativeobj(data,swap(route,rnd[0],rnd [1]))
print(timeit.default_timer() - start_time) """







"""

print('After two opt incere: '+str(incrementaltwopt(data,obj,route,rnd[0],rnd[1])))
route = twoopt(route, rnd[0], rnd[1])
print(route)
print('After two opt Iterative: '+str(iterativeobj(data,route)))  """
"""
start_time = timeit.default_timer()

for i in range(100000):
  incrementaltwopt(data,obj,route,rnd[0],rnd[1])

print(timeit.default_timer() - start_time)


start_time = timeit.default_timer()
for i in range(100000):
  iterativeobj(data,route)
print(timeit.default_timer() - start_time)"""


city = list()
city.append("A")
city.append("B")
city.append("C")
city.append("D")
city.append("E")
city.append("F")

print(threeopt(route,0,2,5))






