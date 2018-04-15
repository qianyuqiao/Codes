#/usr/bin/python
from kombu import Queue,Exchange
from kombu.messaging import Consumer
from kombu.connection import Connection


def process_data(body,msg):
    print msg.payload
    msg.ack()

try:
    connection=Connection('amqp://guest:767918@192.168.8.108:5672//')
except Exception:
    raise

channel=connection.channel()

_exchange = Exchange('neutron',type='topic',channel=channel,durable=False,auto_delete=True,exclusive=False)
video_queue = Queue('',exchange=_exchange,routing_key='q-plugin',channel=channel)
consumer=Consumer(channel,queues=[video_queue],callbacks=[process_data])
consumer.consume()

while True:
    connection.drain_events(timeout=None)

consumer.cancel()

