from functools import partial
def add(a,b):
    return a+b

addOne=partial(add,1)


print addOne(2)
