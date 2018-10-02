import sys
class A(object):
    
    def __init__(self, name):
        self._name = name

    def PrintA(self):
        print self._name
    

def test(cls_name):

    ACLASS = getattr(sys.modules['__main__'], cls_name)
    a = ACLASS('das')
    a.PrintA()

test('A')
