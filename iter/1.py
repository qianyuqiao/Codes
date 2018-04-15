class A(object):
    def __init__(self):
        self.index=0
        self.limit=10


    def __iter__(self):
        return self

    def next(self):
        if self.index<10:
            m=self.index
            self.index+=1
            return m
        else:
            raise StopIteration

a=A()
a=iter(a)
print next(a)
print next(a)
