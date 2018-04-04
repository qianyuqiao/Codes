import eventlet
from eventlet import greenthread
from abc import ABCMeta
import os
def generate(limit=100):
    if limit>100:
        print 'limit exceeded!'
        return
    else:
        for i in range(limit):
            print 'limit=',limit,'the number is ',i
    return 
def hello(gt):
    print 'finished!'
    
def func2():
    pool=eventlet.GreenPool()
    green_generate=pool.spawn(generate())
    green_generate.link(hello)
    pool.waitall()

class MyABC(object):
    def get_type(self):
        pass
  
    def init(self):
        pass

l=['a','b','c']
def gentest():
    i=0
    while i<3:
        yield l[i]
        i+=1
class GenClass(object):
    def __init__(self):
        pass
    def __iter__(self):
        return self
    def next():
        print 2
def readfile():
    with open(os.path.join(os.path.dirname(__file__),'t.conf')) as f:
        for line in f.readlines():
            print line

def pkg():
    from pkg_resources import iter_entry_points
    for ep in iter_entry_points(group='cms.plugin',name=None):
        print ep
class A(object):
    def __init__(self):
        super(A,self).__init__()
        print 'A object initialized finished!'

if __name__ == '__main__':
    a=A()
