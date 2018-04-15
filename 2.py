class A(object):
    
    def print_a(self):
        print 'print_a method was called!'

    def  print_b(self):
        print 'print_b method was called!'

    def print_c(self):
        print 'print_C method was called!'


    _METHOD_MAP={
    'printa':print_a,
    'printb':print_b,
    'printc':print_c
    }


def main():
    
    a=A()
    names=['printa','printb','printc']
    methods= []
    
    for name in names:
        methods.append(a._METHOD_MAP.get(name))

    [ method(a) for method in methods]


if __name__ == '__main__':
    main()
