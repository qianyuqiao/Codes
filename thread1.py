import thread
from time import sleep,ctime


def loop1():
    print 'start loop1'
    sleep(3)
    print 'loop1 done'



def loop2():
    print 'start loop2'
    sleep(3)
    print 'loop2 done'

def main():
    
    print 'begin main thread'
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())

    sleep(10)

    print 'main done'
    
if __name__ == '__main__':
    main()

