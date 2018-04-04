from kombu import Connection
from kombu import Exchange
from kombu import Queue
text_exchange=Exchange('text','direct',durable=True)
txt_queue=Queue('txt',exchange=text_exchange,routing_key='txt')
def process_text(body,messgae):
    print body
    message.ack()

with Connection('amqp://guest:123456@localhost//') as conn:
    producer = conn.Producer(serializer='json')
    producer.publish({'name':'/tmp/1.txt'},exchange=text_exchange,declare=[txt_queue])
    with conn.Consumer(txt_queue,callbacks=[process_text]) as consumer:
        while True:
            conn.drain_events()


