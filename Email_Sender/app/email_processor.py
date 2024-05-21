
import pika, sys, os
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    HOST = os.getenv("HOST_RABBITMQ")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
           
            message_content = body.decode()
           

           

            ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='task_queue', 
                          on_message_callback=callback, 
                         )

    print(' [*] Đang chờ tin nhắn. Nhấn CTRL + C để thoát.')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Kết thúc!!!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)