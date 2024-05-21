import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_email_data(email_id):
    KEY_API = os.getenv("GET_EMAIL")
    url = f"{KEY_API}/{email_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Lỗi", f"Không thể kết nối tới API để lấy dữ liệu email: {e}")
        return None

def update_status(email_id, new_status: str):
    # Lấy dữ liệu hiện tại của email
    email_data = get_email_data(email_id)
    # Cập nhật trạng thái
    email_data["email"]["status"] = new_status
    # Gửi yêu cầu PUT để cập nhật email
    KEY_API = os.getenv("UPDATE_EMAIL")
    url = f"{KEY_API}/{email_id}"
    try:
        response = requests.put(url, json=email_data)
        response.raise_for_status()
        if response.status_code == 200:  
            print("Email cập nhật trạng thái thành công!")
        else:
            error_message = response.json().get('detail', response.text)
            print("Lỗi", f"Đã xảy ra lỗi: {error_message}")

    except requests.exceptions.RequestException as e:
       print("Lỗi", f"Không thể kết nối tới API: {e}")

