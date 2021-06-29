import pika
import emailhandler

url = #enter url of queue
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='event') # Declare a queue

def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))
    try:
        emailhandler.registration_email(body)
    except Exception as e:
        print(e.message)

channel.basic_consume('event',callback,auto_ack=True)
print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()