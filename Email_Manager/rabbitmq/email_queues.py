#email_queue.py
import pika
from dotenv import load_dotenv
import os,json
load_dotenv() 
from database.schemas import RequestMail

HOST = os.getenv("HOST_RABBITMQ")

def send_message_to_queue(request:RequestMail,id):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = HOST))
    channel = connection.channel()
    channel.queue_declare(queue = 'task_queue', durable = True)
    request_dict = request.dict()
    # Chuyển đổi 'create_at' thành chuỗi có thể chuyển đổi sang JSON
    request_dict['email']['create_at'] = request_dict['email']['create_at'].isoformat()
    # Thêm trường 'id' vào message
    request_dict['email']['id'] = id
    message = json.dumps(request_dict)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body = message,
        properties=pika.BasicProperties(
            delivery_mode= pika.DeliveryMode.Persistent  
        )
    )
    print(f" [x] Sent {message}")
