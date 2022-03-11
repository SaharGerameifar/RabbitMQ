import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='second', durable=True)
channel.basic_publish(exchange='', routing_key='second', properties=pika.BasicProperties(delivery_mode=2), body='this is a second test.')
print('message sent.')
connection.close()

