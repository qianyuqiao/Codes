import  thread

from  time  import sleep , ctime

sleep_times=[1,2,3]

def loop(num,sleep_time,lock):

    print 'starting loop %s at %s '%(str(num), ctime())
    
    sleep(sleep_time)
    lock.release()

    print 'finished running loop %s at %s'%(str(num),ctime())



def main():

    locks=[]


    for i in range(len(sleep_times)):
        lock= thread.allocate_lock()
        lock.acquire()
        locks.append(lock)


    for i in range(len(sleep_times)):

        thread.start_new_thread(loop,(i,sleep_times[i],locks[i]))


    for i in range(len(sleep_times)):
        while locks[i].locked():
            pass 


    print 'all done at %s'%(str(ctime()))



if __name__ == '__main__':
    main()
