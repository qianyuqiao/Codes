from kombu.entity import Exchange
from kombu.messaging import Producer
from kombu.connection import Connection
from time import sleep

connection= Connection('amqp://guest:767918@192.168.8.108:5672//')
channel=connection.channel()

_exchange=Exchange('media','direct',channel)
producer=Producer(channel,exchange=_exchange,routing_key='video')
for i in range(10):
    producer.publish({'name':'fuckyou.avi','size':13131})
    print 'published!'
    sleep(1)

