import eventlet
from eventlet import wsgi
from hook import hook
import time
import sys,os
import socket
interval=30
eventlet.monkey_patch()

def run_with_cgi(app):

    environ = dict(os.environ.items())
    environ['wsgi.input']        = sys.stdin
    environ['wsgi.errors']       = sys.stderr
    environ['wsgi.version']      = (1, 0)
    environ['wsgi.multithread']  = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once']     = True

    if environ.get('HTTPS', 'off') in ('on', '1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    def write(data):
        if not headers_set:
             raise AssertionError("write() before start_response()")

        elif not headers_sent:
             # Before the first output, send the stored headers
             status, response_headers = headers_sent[:] = headers_set
             sys.stdout.write('Status: %s\r\n' % status)
             for header in response_headers:
                 sys.stdout.write('%s: %s\r\n' % header)
             sys.stdout.write('\r\n')

        sys.stdout.write(data)
        sys.stdout.flush()

    def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    # Re-raise original exception if headers sent
                    raise exc_info[0], exc_info[1], exc_info[2]
            finally:
                exc_info = None     # avoid dangling circular ref
        elif headers_set:
            raise AssertionError("Headers already set!")

        headers_set[:] = [status, response_headers]
        return write

    result = app(environ, start_response)
    try:
        while True:
            for data in result:
                if data:    # don't send headers until body appears
                    write(data)
            if not headers_sent:
                write('')   # send headers now if body was empty
    except Error:
        pass
    finally:
        if hasattr(result, 'close'):
            result.close()



def  neutron_app(env,start_response):
    if env['PATH_INFO']!='/':
        start_response('404 not found!',[{'Content-Type','text/plain'}])
        return ['404 Not Found\r\n']
    start_response('200 OK',[{'Content-Type','text/plain'}])
    return ['Hello, world !\r\n']


    
class Server(object):
    def __init__(self,name):
        self.pool=eventlet.GreenPool()
        self.name=name
        self._launcher=None
        self._server=None
    def _get_socket(self,host,port,backlog):
        bind_addr=(host,port)
        try:
            info= socket.getaddrinfo(bind_addr[0],bind_addr[1],socket.AF_UNSPEC,socket.SOCK_STREAM)[0]
            family=info[0]
        except Exception as e:
            print 'in _get_socket,',e
        sock=None
        retry_until=time.time()+interval
        while not sock and time.time()<retry_until:
            try:
                sock=eventlet.listen(addr=bind_addr,backlog=backlog,family=family)
            except Exception as err:
                print 'in eventlet.listen,',err
                eventlet.sleep(0.1)
        if not sock :
            raise RunTimeError('Could not bind to the port')
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_KEEPALIVE,1)
        return sock
    def start(self,application,port=9696,host='0.0.0.0',workers=0):
        self._host=host
        self._port=port
        backlog=10
        self._socket=self._get_socket(self._host,self._port,backlog=backlog)
        if workers<1:
#            self._server = self.pool.spawn(self._run,application,self._socket)
            run_with_cgi(application)           

    def wait(self):
        try:
            self.pool.waitall()
        except KeyboardInterrupt:
            pass
    def _run(self,application,socket):
        wsgi.server(socket , application , custom_pool=self.pool , keepalive=True)

def _run_wsgi(app_name):
    server=Server(app_name)
    server.start(neutron_app)
    return server

class NeutronApiService(object):
    def __init__(self,app_name):
        self.app_name=app_name
        self.wsgi_app=None
    def start(self):
        self.wsgi_app=_run_wsgi(self.app_name)
    def wait(self):
        self.wsgi_app.wait()

def serve_wsgi(cls):
    try:
        if not isinstance(cls,type):
            print 'cls should be a type'
            raise
        else:
            service=cls('neutron')
            service.start()
            return service
    except Exception as e:
        print 'in serve_wsgi,',e

def main():
    try:
    #    pool=eventlet.GreenPool()
        serve_wsgi(NeutronApiService)
        #api_thread=pool.spawn(neutron_api_server.wait)
    #    pool.waitall()
    except Exception as e:
        print e

if __name__=='__main__':
    main()
