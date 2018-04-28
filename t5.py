class A(object):
    _num= 0
    def __init__(self):
        pass 


a0=A()
print a0._num
print 'now we change the number'
A._num= 1
a1=A()
print a1._num
