args = {}
args['name'] = 'jack'
args['id'] = 12345
a = 1
b = 1
def test(**args):
    print args
    
test(a, b)
