import eventlet
from eventlet import wsgi
import argparse
import datetime



def hello_world(env, start_response):
    if env['PATH_INFO'] != '/':
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ['Not Found\r\n']
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World!\r\n']


def test():
    parser=argparse.ArgumentParser()
    parser.add_argument('--addall',default=True , help='accumulate all numbers')
    result , remains = parser.parse_known_args()
    return  result.func

class MyException(Exception):
    pass 


def _help(x):
    if x == 1:
        
        raise MyException('x=1')

def main():
    try:
        _help(1)

    except MyException as e:
        print e
    
    print 'done!'


def utc2local(utc_dt):
    if not isinstance(utc_dt,datetime.datetime):
        raise TypeError()

    utc=datetime.datetime.utcnow()
    local= datetime.datetime.now()
    offset = local  - utc
    local_dt = utc_dt + offset
    return local_dt


def local2utc(local_dt):

    if not isinstance(local_dt,datetime.datetime):
        raise TypeError()
    
    utc=datetime.datetime.utcnow()
    local= datetime.datetime.now()
    offset =  utc - local
    utc_dt  = utc_dt + offset
    return utc_dt

def tt():
    pass

def selfadd(num):
    return num+1

a= test()
print a
