from eventlet import wsgi
import eventlet
def hello(env,start_response):
    start_response('200 OK',[{'Content-Type','text/plain'}])
    return ['Hello World!\r\n']

wsgi.server(eventlet.listen(('0.0.0.0',9999)),hello)
