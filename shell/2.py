#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import subprocess
import shlex

"""
这段代码实现了对子进程的实时打印到屏幕上
"""

PIPE =subprocess.PIPE

def main():

    #下面这段代码是输出产生器
    _cmd= 'python generate.py'
    cmd= shlex.split(_cmd)
    p=subprocess.Popen(cmd,shell=False,stdout=PIPE,stderr=PIPE)
    while p.poll() is  None:
        
        line=p.stdout.readline()
        line=line.strip()
        if line:
            print 'subprocess.output:{}'.format(line)
    
    if p.returncode == 0:
        print 'subprocess succeed'
    else:
        print 'subporcess failed'

if __name__ == '__main__':
    main()
