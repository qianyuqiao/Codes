#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import threading
from  time import sleep

from eventlet.green import subprocess
PIPE=subprocess.PIPE


def _subprocess_popen(args,shell=False,stdin=None,stdout=None,stderr=None):
    
    return subprocess.Popen(args,shell=shell,stdin=stdin,stdout=stdout,stderr=stderr)

"""
下面这个例子讲的是非阻塞式的调用子进程，当调用命令行后，可以观察到，还是打印出了那行英文
"""
def test1():

    popen=_subprocess_popen(['popen'],shell=False ,stdout=PIPE,stderr=PIPE)
    
    print 'happens while running'
    
    #由于readline()是对PIPE文件进行读取，等到文件释放掉锁后(虽然释放锁具体的实现机制我也不清楚)，才能对文件进行读取
    data = popen.stdout.readline()

    return data

def test2():

    popen=_subprocess_popen(['popen'],shell=False ,stdout=PIPE,stderr=PIPE)

    #由于先等待所有子进程返回后才能继续进行主进程，故本段代码过一段时间后才会打印下面这段英文
    popen.wait()
    
    print 'happens while running'
    
    data = popen.stdout.readline()

    return data


def read_on_write():

    def write_thread():
        
        f=open('/home/qianyuqiao/codes/2.py','w')
        
        for i  in range(10):
            print 'begin writing'
            f.write(str(i)+'\n')
            print 'write %s'%str(i)
            sleep(1)

        f.close()
    
    wthread=threading.Thread(target=write_thread)
    wthread.start()

    try:
        f1=open('/home/qianyuqiao/codes/2.py','r')
        print 'main thread run!'
        for line  in f1.readlines():
            print 'the output: %s'%str(line)
            sleep(1)
       
        f1.close()
        print 'f1 closed'
    except Exception as e:
        print 'Exception occured! it is %s'%str(e)
        

def main():

    stdout  = test2()
    #print 'the stdout is %s'%str(stdout)

if __name__ == '__main__':
    main()
