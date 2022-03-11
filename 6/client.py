import pika
import uuid


class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))        
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_response, auto_ack=True)
       
    def on_response(self, ch, method, properties, body):
        if self.correlation_id == properties.correlation_id:
            self.response = body

    def call(self, a, b):
        self.response = None
        self.correlation_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='', routing_key='rpc', properties=pika.BasicProperties(reply_to=self.queue_name, correlation_id=self.correlation_id), body=str(a)+"."+str(b))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


obj = Sender()
response = obj.call(4, 5)      
print(response)
