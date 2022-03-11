import pika
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='log', exchange_type='direct')
result = channel.queue_declare(queue='', exclusive=True, durable=True)
queue_name = result.method.queue
serverities = ('info', 'error', 'warning')

for serverity in serverities:
	channel.queue_bind(exchange='log', queue=queue_name, routing_key=serverity)

def callback(ch, method, properties, body):
	sleep(5)
	print(f'****{body}****')
	channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=queue_name, on_message_callback=callback)
print('waiting for logs, to exit press ctrl+c')
channel.start_consuming()


