import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

 
def submit_info():
    email_from = from_entry.get()
    email_to = to_entry.get()
    subject = subject_entry.get()
    email_content = email_entry.get("1.0", tk.END).strip() 
   
    create_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{create_at}")
    data = {
        "email": { 
            "email_from": email_from,
            "email_to": email_to,
            "subject": subject,
            "content": email_content,
            "status": "Đang gửi",
            "create_at":create_at
        }
    }
    KEY_API = os.getenv("POST_EMAIL")
    try:
        response = requests.post(KEY_API, json=data)
        response.raise_for_status() 

        if response.status_code == 200:  
            messagebox.showinfo("Thành công", "Email đã được gửi thành công!")
        else:
            error_message = response.json().get('detail', response.text)
            messagebox.showwarning("Lỗi", f"Đã xảy ra lỗi: {error_message}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Lỗi", f"Không thể kết nối tới API: {e}")

root = tk.Tk()
root.title("Gửi Email")
root.geometry("500x600")

email_from = tk.Label(root, text="From:")
email_from.pack(pady=5)
from_entry = tk.Entry(root, width=50)
from_entry.pack(pady=5)


email_to = tk.Label(root, text="To:")
email_to.pack(pady=5)
to_entry = tk.Entry(root, width=50)
to_entry.pack(pady=5)

subject = tk.Label(root, text="Subject:")
subject.pack(pady=5)
subject_entry = tk.Entry(root, width=50)
subject_entry.pack(pady=5)

email_content = tk.Label(root, text="Nội dung Email:")
email_content.pack(pady=5)
email_entry = tk.Text(root, height=10, width=50)
email_entry.pack(pady=5)

submit_button = tk.Button(root, text="Gửi", command=submit_info)
submit_button.pack(pady=20)

root.mainloop()
