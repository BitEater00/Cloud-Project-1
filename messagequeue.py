import pika
def uploadQueueClub(studentId):
    url = #enter url
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() 
    channel.queue_declare(queue='club')
    channel.basic_publish(exchange='',routing_key='club',body = studentId)
    connection.close()

def uploadQueueEvent(studentId):
    url = #enter url
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() 
    channel.queue_declare(queue='event')
    channel.basic_publish(exchange='',routing_key='event',body = studentId)
    connection.close()