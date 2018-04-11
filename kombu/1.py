#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
这段代码实际上是kombu包的一个例程，展示了发送与接受消息的一个流程
"""
from kombu  import Connection,Exchange,Queue
from kombu.messaging import Consumer,Producer
import threading
from time import sleep
import socket

def main():

    def echo_process(body,message):
        print body 
        message.ack()


    uni_exchange = Exchange('university','direct',durable=True)
    c9_queue = Queue('c9', exchange=uni_exchange, routing_key='c9')
    
    with Connection('amqp://guest:767918@localhost:5672//') as conn:
        print 'connection succeeded!'
        channel1 = conn.channel()
        _exchange =  uni_exchange

        def produce_msg():
            producer= Producer(channel1,exchange=_exchange,routing_key='c9')
            for _ in range(5):
                producer.publish({'name':'xjtu',
                        'status':'c9'})
                sleep(1)


        _thread= threading.Thread(target=produce_msg)

        with Consumer(channel1,queues=[c9_queue],callbacks=[echo_process]) as consumer:
            consumer.consume()
            print 'consumer began consuming!'
            
            _thread.start()
            while True:
                print 'will run connection.drain'
                try:
                    conn.drain_events(timeout=3)
                except socket.error :
                    print 'socket timeout!'
                    break

                print 'get msg'
            
            consumer.cancel()
    
    
if __name__ == '__main__':
    main()
