import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='first')
channel.basic_publish(exchange='', routing_key='first', body='this is a first test.')
print('message sent.')
connection.close()

