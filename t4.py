import time
import eventlet
from eventlet import event
from eventlet import greenthread
evt=event.Event()
def jocker():
    i=0;
    while i<3:
        print 'jocker: can anybody catch me?'
        i+=1
        time.sleep(1)
    print evt.wait()
    print  'fighting!'
    time.sleep(3)
    return 'jocker: sorry, you got missed!'

def batman():
    evt.send('batman: i am coming for you!')
    return 'batman; I am back, and your day is coming!'

gt1=greenthread.spawn(jocker)
gt2=greenthread.spawn_after(5,batman)

print gt1.wait()
time.sleep(1)
print gt2.wait()
time.sleep(1)
print 'to be continued.............'
