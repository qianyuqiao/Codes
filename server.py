from  wsgiref.simple_server import  make_server 
from  eventlet import greenthread
import eventlet

def handle_request(env,res):
    sleep(5)
    res('200 OK',[('Content-Type','text/html')])
    body = 'hello world'

    return [body.encode('utf-8')]


def main():

    
    httpd= make_server('',8000,handle_request)
    print 'serving http on port 8000'
    httpd.serve_forever()

if __name__ == '__main__':

    pool = eventlet.GreenPool()
    gt=pool.spawn(main())
    pool.waitall()
