import socket
EOL1=b'\n\n'
EOL2=b'\n\r\n'
response=b'HTTP/1.0 200 OK\r\nDate:Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response+=b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n' 
response+=b'hello,world!'

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind(('127.0.0.2',8080))
serversocket.listen(1)
try:
    while True:
        connection,addr=serversocket.accept()
        print 'addr: ',str(addr)
        request=b''
        while EOL1 not in request and EOL2 not in request:
            request+=connection.recv(1024)
        print '-'*40+'\n'+request.decode()[:-2]
        connection.send(response)
        connection.close()
finally:
    serversocket.close()
