# ỨNG DỤNG GỬI EMAIL SỬ DỤNG RABBITMQ

## Mô tả 

### Phân tích 

* Service 1: Email_Manager: 

1. Tạo endpoint API post để nhận yêu cầu gửi email với thông tin như: email người gửi, email người nhận, tiêu đề email, nội dung email.

2. Tạo một endpoint API put cho phép Service 2 cập nhật trạng thái email (thành công hoặc thất bại) sau khi gửi.

3. Lưu trữ thông tin gửi email và trạng thái của chúng vào cơ sở dữ liệu PostgreSQL.

4. Mỗi yêu cầu sẽ được đẩy vào hàng đợi (queue)

* Service 2: Email_Sender:

1. Kết nối tới RabbitMQ và lắng nghe hàng đợi để nhận các nội dung về các email.

2. Tiến hành gửi email sử dụng thư viện Resend để gửi email với thông tin nhận được từ hàng đợi.

3. Xử lý kết quả gửi email (thành công hoặc thất bại) bằng cách gọi endpoint API put của Service 1 để cập nhật trạng thái của email.

### Công ghệ sử dụng 

- Ngôn ngữ Python
- Tạo API bằng FastAPI.
- Lưu trữ dữ liệu email bằng PostgreSQL.
- Dùng Docker làm server.
- Phần mềm trung gian RabbitMQ.
- Sử dụng Resend để gửi đến email thật.

### Sơ đồ luồng hoạt động.
![markdown](https://github.com/truong270801/translate_Intern/blob/main/rabbitmq_sendmail.png)

## Cài đặt và chạy chương trình
### Yêu cầu :
* Cài đặt [Python](https://www.python.org/downloads/)
* Cài đặt [PostgreSQL](https://www.postgresql.org/download/)
* Tùy nhu cầu dùng [Postman](https://www.postman.com/downloads/)
* Cài đặt [Docker](https://www.docker.com/products/docker-desktop/)

### Cài đặt :

* `git clone https://github.com/truong270801/rabbitmq_sendmail.git`

#### Cơ sở dữ liệu:
* Tạo cơ sở dữ liệu mới tên là `Users`
* Sửa đổi tên, mật khẩu, tên database, tên host trong file .env
```
DB_USER="postgres"
DB_PASS="123456"
DB_HOST="localhost:5432"
DB_NAME="Users"
```
#### Mở lệnh Terminal VSCode:
```
cd rabbitmq_sendmail
pip install pika
pip install uvicorn
pip install fastapi
pip install python-dotenv
pip install sqlalchemy
pip install psycopg2
pip install tkinter
pip install resend

```
### Chạy chương trình
```
//chạy Docker: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management

- Service 1 :
    + Chạy FastAPI 
        cd Email_Manager
        cd app
        uvicorn main:app --reload
    + Chạy UI nhập tin nhắn :
        cd Email_Manager
        cd app
        cd UI
        python email_ui.py
- Service 2 :
    cd Email_Sender
    cd app
    python email_processor.py

```