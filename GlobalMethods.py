#swap
def swap(rt, f, s):
  temp = rt[f]
  rt[f] = rt[s]
  rt[s] = temp
  return rt
#2-opt
def twoopt(rt, f, s)
  f = f+1
  while f < s:
    rt = swap(rt, f, s)
    s -= 1
    f += 1
    return rt
#k-opt
  ???
#iterative objective
def iterativeobj(distances, rt):
  obj = distances[rt[0]][rt.shape-1]
        for i in range(rt.shape-1):
            obj += distances[rt[i]][rt[i+1]]
        return obj

#incremental objective
def incrementalobj(distances,obj,rt,f,s)
    
