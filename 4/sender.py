import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='log', exchange_type='direct')
messages = {
    'info': 'this is Info message.',
    'error': 'this is Error message.',
    'warning': 'this is Warning message.',
}
for key, value in messages.items():
    channel.basic_publish(exchange='log', routing_key=key, body=value)
    
print('message sent.')
connection.close()

