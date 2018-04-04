import itertools
def func1():
    natuals=itertools.count(1)
    for n in natuals:
        if n>10 :
            break
        print n

def func2(limit=10):
    next_indice=itertools.cycle(range(limit))
    for i in range(limit):
        print next(next_indice)

if __name__ == '__main__':
    func2()
