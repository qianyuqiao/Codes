from tt import A
def main(A):
    if isinstance(A,type):
        print 'A is the class, the name is ',A.__name__
    else:
        print 'A is not a class !'

main(A)
