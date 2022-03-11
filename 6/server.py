import pika
from time import sleep


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc')


def callback(ch, method, properties, body):
	body = body.decode('UTF-8')
	x = body.split(".")
	a = int(x[0])
	b = int(x[1])
	sleep(4)
	response = a + b
	channel.basic_publish(exchange='', routing_key=properties.reply_to, properties=pika.BasicProperties(correlation_id=properties.correlation_id), body=str(response))
	channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc', on_message_callback=callback)
print('waiting for request, to exit press ctrl+c')
channel.start_consuming()
