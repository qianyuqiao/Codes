from kombu.entity import Exchange
from kombu.messaging import Producer
from kombu.connection import Connection
from time import sleep
import sys


connection= Connection('amqp://guest:767918@localhost:5672//')
channel=connection.channel()

def main():
    
    _exchange=Exchange('media','direct',channel)
    producer=Producer(channel,exchange=_exchange,routing_key='video')
    
    for i in range(10):
        producer.publish({'name':'fuckyou.avi','size':13131})
        print 'published!'
        sleep(1)

def main1():
    
    _exchange=Exchange('media1',type='fanout',durable=False)
    
    producer = Producer(channel,exchange=_exchange)

    for i in range(10):
        producer.publish({'name':'fuckme.avi',
                          'size':13131})
        
        sys.stdout.write('published!\n')
        sleep(1)

if __name__ == '__main__':
    main1()
