import time

def timewrapper(func):
    def inner(*args, **kwargs):
        st = time.time()
        ret = func(*args, **kwargs)
        ed = time.time()
        print "time is %s " % (ed - st)
        return ret
    return inner

def a(line):
    if line.startswith("Hosts"):
        pass


def b(line):
    if line[:5] == "Hosts":
        pass

@timewrapper
def testa():
    f = open("1.txt", "r")
    for line in f.readlines():
        a(line)
    f.close()
    

@timewrapper
def testb():
    f = open("1.txt", "r")
    for line in f.readlines():
        b(line)
    f.close()

testa()
testb()
