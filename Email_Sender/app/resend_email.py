import os
from dotenv import load_dotenv
import resend

def send_email(email_from, email_to, subject, content):
  load_dotenv()
  resend.api_key = os.getenv("KEY_RESEND")

  r = resend.Emails.send({
        "sender": f"{email_from}",
        "to": f"{email_to}",
        "subject": f"{subject}",
        "html": f"<p>{content}</p>"
  })
  print("Đã nhận tin nhắn và gửi tới Email!!")