from myovs import utils 
import greenlet
from wsgi_ref.simple_server import  make_server 
import requests

def my(myname,*args):
    print 'myname: ',str(myname)
    print 'args: ',str(args)

def test_greenlet_tracing():

    def  dummy(x,y):
        
        z = gr2.switch(x+y)


    def dummy_exception():

        assert  False

    gr1=greenlet.greenlet(test1)
    gr2=greenlet.greenlet(test2)


def handle_request(env,res):
    
    res('200 OK',[('Content-Type','text/html')])
    body = 'hello world'

    return [body.encode('utf-8')]


def server(request):
    sleep(5)
    return str(request).upper()


def async_call():
    
    def greentify(func):

        gr=greenlet.greenlet(func)
        return gr

    @greentify
    def foo(request):
        url='219.245.186.204:8000'
        rsp = requests.get(url)
        print 'get response %s'%str(a)
        return a

    print 'begin requesting'
    foo.switch('hello world')

    gt.wait()
    print 'now I am hanging out'



def main():
    
    httpd= make_server('',8000,handle_request)
    print 'serving http on port 8000'
    httpd.serve_forever()


if __name__ == "__main__":
    async_call()
