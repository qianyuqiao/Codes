def printkwargs(**kwargs):
    name = kwargs.get('name', None)
    if name:
        print 'name is in the kwargs'
    else:
        print 'name not in'

def printargs(*args):
    name = args[0]
    print name

printkwargs(name='sb')
printargs('sb')
