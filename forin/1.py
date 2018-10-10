class A(object):
    pass
mylist = []
for _ in range(5):
    mylist.append(A())

def add_name_to_obj(obj, name):
    obj.name = name

for x in mylist:
    add_name_to_obj(x, 'tony')

print [ x.name for x in mylist]

a = A()
