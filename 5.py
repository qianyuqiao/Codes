class A(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

class Mylist(list):
    
    def __contains__(self,obj):
        for i in self:
            if isinstance(obj,i.__class__):
                if i.a== obj.a and  i.b == obj.b:
                    return True
            
        return False


mylist= Mylist()
mylist.append(A('2','2'))
a1=A('1','2')
if a1 in mylist:
    print 'yes'
else:
    print 'No'


