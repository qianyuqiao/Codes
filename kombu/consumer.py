#/usr/bin/python
from kombu import Queue,Exchange
from kombu.messaging import Consumer
from kombu.connection import Connection
import  socket
import sys
import eventlet
from eventlet import greenthread
from time import sleep
import traceback


def process_data(body,msg):
    print str(msg.payload)
    msg.ack()


eventlet.monkey_patch()

connection=Connection('amqp://guest:767918@localhost:5672//')
channel=connection.channel()


def main():

    def error_callback(func):

        def _inner(*args,**kwargs):    

            try:
                func(*args,**kwargs)

            except Exception as exc:

                if isinstance(exc,socket.timeout):
                    sys.out.write('socket timeout occured in exec')

                else:
                    raise exc
        
        return  _inner 


    @error_callback
    def _consume():

        sys.stdout.write('yes  666666\n')
        _exchange = Exchange('media1',type='fanout',channel=channel,durable=False)
        video_queue = Queue('video',exchange=_exchange,routing_key='video',channel=channel)
        consumer=Consumer(channel,queues=[video_queue],callbacks=[process_data])
        consumer.consume()
        
        while True:
            try:
                connection.drain_events()
            
            except socket.timeout:
                consumer.cancel()
                break
                raise


        #actually ,it cancelled the connection 
        consumer.cancel()

    try:

        print 'begining!'

        eventlet.spawn(_consume)
        
        print 'I will sleep for 10  seconds'
        
        eventlet.sleep(10)
        
        print 'main thread finished!'
    
    except Exception :
        traceback.print_exc()


if __name__ == '__main__':
    main()
