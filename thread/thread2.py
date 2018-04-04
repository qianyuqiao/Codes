from  time  import sleep,ctime
from threading import Thread

exit_num = 0

class MyThread(Thread):

    def __init__(self,name,s_time,count):

        Thread.__init__(self)
        self.name=name
        self.s_time=s_time
        self.count = count


    def run(self):
        print 'start running Thread %s'%str(self.name)
        self.print_time(self.count)
        print 'finished running Thread %s'%str(self.name)

    def print_time(self,count):

        while True:

            if count == 0 :
                break

            sleep(self.s_time)
            print '%s : %s '%(self.name,ctime())
            count -=1


def main():
    
    td1 = MyThread('Thread1',2,5)
    td2=  MyThread('Thread2',5,5 )
    td1.start()
    td2.start()

if __name__  == '__main__':
    main()
