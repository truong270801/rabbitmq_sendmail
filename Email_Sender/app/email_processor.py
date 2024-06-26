
import pika, sys, os
import json
from resend_email import send_email
from email_status import update_status

from dotenv import load_dotenv
import os
load_dotenv()

def main():
    HOST = os.getenv("HOST_RABBITMQ")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
            # Giải mã nội dung của tin nhắn từ dạng bytes sang chuỗi
            message_content = body.decode()
            # Phân tích chuỗi JSON thành một đối tượng từ điển Python
            message_dict = json.loads(message_content)

            email_id = message_dict ['email']['id']
            email_from = message_dict['email']['email_from']
            email_to = message_dict['email']['email_to']
            subject = message_dict['email']['subject']
            content = message_dict['email']['content']
           
            try:
                    send_email(email_from, email_to, subject, content)
                    update_status(email_id, "Thành công")
            except Exception as e:
                    update_status(email_id, "Thất bại")

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