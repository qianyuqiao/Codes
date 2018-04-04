from kombu import Connection,Exchange,Queue
import sys

class A(object):
    name='default name'
    def __init__(self,name=''):
        self.name=name or self.name
    

def test():
    try:
        print 2/0
    except Exception as e:
        print e
        sys.exit(0)
    print 'after exception handle!'

def rabbitmq():
    pika=__import__('pika')
    connection = pika.BlockingConnection(pika.ConenctionParameters('localhost'))
    channel=connection.channel()
    channel.queue_declare()

def kombu():
    text_exchange = Exchange('text','direct',durable=True)
    txt_queue = Queue('txt',exchange=text_exchange,routing_key='text')
    with Connection('amqp://guest:123456@localhost//') as conn:
        producer=conn.Producer(serializer='json')
        producer.publish({'name':'/tmp/1.txt'},exchange=text_exchange,routing_key='text',declare=[txt_queue])
    

def process_media(body,message):
    print body
    message.ack()

if __name__ == '__main__':
    test()
