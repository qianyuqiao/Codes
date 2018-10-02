class A(object):
    
    def __new__(cls,a):
        print '__new__ was called!'
        return super(A,cls).__new__(cls,a)

    def __init__(self,a):
        print '__init__ was called!'
        self.a = a

    def __str__(self):
        return '<A:%s>'%self.a

if __name__ =='__main__':
    a=A('helloworld')
    print a
