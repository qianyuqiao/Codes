import hubs
from greenthread import GreenThread

def spawn(func,*args,**kwargs):
    
    hub= hubs.get_hub()
    g= GreenThread(hub._greenlet)
    hub.schedule_call_glocal(0,g,switch,func,args,kwargs)
    return g
