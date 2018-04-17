#/usr/bin/python
from kombu import Queue,Exchange
from kombu.messaging import Consumer
from kombu.connection import Connection


def process_data(body,msg):
    print str(msg.payload)
    msg.ack()
def main():
    try:
        connection=Connection('amqp://guest:767918@192.168.8.108:5672//')
    except Exception:
        raise
    print 'connecting to amqp server succeed!'

    channel=connection.channel()

    _exchange = Exchange('media',type='direct',channel=channel)
    video_queue = Queue('video',exchange=_exchange,routing_key='video',channel=channel)
    consumer=Consumer(channel,queues=[video_queue],callbacks=[process_data])
    consumer.consume()

    while True:
        connection.drain_events(timeout=10)

    consumer.cancel()
if __name__ == '__main__':
    main()
