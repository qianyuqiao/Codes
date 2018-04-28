from greenlet import greenlet
import hubs

class GreenThread(greenlet):

    def __init__(self,parent):
        greenlet.__init__(self,self.main,parent)
        self._exit_event= 


def spawn(func,*args,**kwargs):
    hub = hubs.get_hub()
    g=GreenThread(hub.)
