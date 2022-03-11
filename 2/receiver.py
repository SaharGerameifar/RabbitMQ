import pika
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='second', durable=True)

def callback(ch, method, properties, body):
	sleep(10)
	print(f'****{body}****')
	channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='second', on_message_callback=callback)
print('Waiting for message, to exit press ctrl+c')
channel.start_consuming()


