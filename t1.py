from routes import Mapper
from routes import middleware
import webob.dec
from wsgiref.simple_server import make_server

class controller(object):
    def __init__(self):
        self.i=1
    def __call__(self):
        print self.i
    def search(self):
        return 'search()'
    def create(self):   #/messages POST
        return 'create()'
    def show(self):    #/messages/{id}  GET 
        return 'show()'    
    def index(self):   #/messages  GET  
        return 'index()'
    def update(self): #/messages/{id}  PUT
        return 'update()'
    def delete(self): #/messages/{id}  DELETE
        return 'delete()'
    def create_many(self):
        return 'create_many()'
    def delete_many(self):
        return 'delete_many()'


class application(object):
    def __init__(self):
        a=controller()
        map=Mapper()
        map.resource('message','messages',controller=a)
        self.route = middleware.RoutesMiddleware(self.dispatch,map)


    @webob.dec.wsgify
    def __call__(self,req):
        return self.route

    @staticmethod
    @webob.dec.wsgify
    def dispatch(req):
        match=req.environ['wsgiorg.routing_args'][1]
        print 'route match result is: ',match
        if not match:
            return 'fake url'

        controller=match['controller']
        action=match['action']
        func=getattr(controller,action,None)
        if func:
            return func()
        else:
            return 'has no action:%s'%action

if __name__ == '__main__':
    app=application()
    server=make_server('',8080,app)
    server.serve_forever()
            
