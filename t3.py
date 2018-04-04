import time
import socket
from concurrent import futures
def nonblocking_way():
    sock=socket.socket()
    sock.setblocking(False)
    while True:
        try:
            sock.connect(('www.baidu.com',80))
            break
        except  IOError:
            pass
    request='GET / HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'
    data=request.encode('ascii')
    while True:
        try:
            sock.send(data)
            break
        except OSError:
            pass
    response=b''
    while True:
        try:
            chunk=sock.recv(4096)
            while chunk:
                response+=chunk
                chunk=sock.recv(4096)
            break
        except OSError:
            pass
    return response

def sync_way():
    res=[]
    for i in range(10):
        res.append(nonblocking_way())
    return len(res)

start=time.clock()
sync_way()
end=time.clock()
print end-start

