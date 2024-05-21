#repo
from sqlalchemy.orm import Session
from model.model import Mail

class mailRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_mail(self, mail_data: dict):
        mail = Mail(**mail_data)
        self.db.add(mail)
        self.db.commit()
        self.db.refresh(mail)
        return mail

    def get_mails(self, skip: int = 0, limit: int = 100):
        return self.db.query(Mail).offset(skip).limit(limit).all()

    def get_mail_by_id(self, mail_id: int):
        return self.db.query(Mail).filter(Mail.id == mail_id).first()

    def update_mail(self, mail_id: int, mail_data: dict):
        mail = self.get_mail_by_id(mail_id)
        if mail:
            for key, value in mail_data.items():
                setattr(mail, key, value)
            self.db.commit()
            self.db.refresh(mail)
        return mail


