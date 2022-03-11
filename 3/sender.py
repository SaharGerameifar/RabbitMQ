import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='log', exchange_type='fanout')
channel.basic_publish(exchange='log', routing_key='', properties=pika.BasicProperties(delivery_mode=2), body='this is a third test.')
print('message sent.')
connection.close()

