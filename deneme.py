

def wrapper(func):
    res = func(10)
    return res

def geometric(t):
    return t * 10

def linear(t):
    return t- 10


names=list()
names.append('geometric')
names.append('linear')

print(wrapper(names[0]))
