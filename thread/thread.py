from  threading import Thread
from time import sleep
class  MyThread(Thread):

    def __init__(self,num):
        
        Thread.__init__(self)
        self.num = num

    def run(self):
        
        print 'start running thread %s'%str(self.num)
    
        print 'in %s , hello python '%str(self.num)
        print 'stop running thread %s'%str(self.num)
    

def bare_thread():
    
    threads=[]
    num=10
    for i in range(num):
        threads.append(MyThread(i))

    for td  in threads:
        td.start()

    print 'all done!'


def daemon_thread():
    threads=[]
    num=10
    for i in range(num):
        threads.append(MyThread(i))
                 
    for td  in threads:
        td.setDaemon(True)
        td.start()

    print 'all done!'


def with_join_set():

    threads=[]
    num=10
    for i in range(num):
        threads.append(MyThread(i))

    for td  in threads:
        td.setDaemon(True)
        td.start()
        td.join()

    print 'all done!'

def with_join_notset():

    threads = []
    num = 10

    for i in range(num):
        threads.append(MyThread(i))

    for td  in threads:

        td.start()
        td.join()


    print 'all done!'

def main():
    #print 'bare thread:'
    #bare_thread()
    #print '\n daemon_thread:'
    #daemon_thread()
    #print '\nset daemon and join:'
    #with_join_set()
    print '\nnot set daemon and join:'
    with_join_notset()

if __name__ == '__main__':
    main()
