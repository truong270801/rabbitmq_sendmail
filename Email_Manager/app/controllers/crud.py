from sqlalchemy.orm import Session
from database.schemas import RequestMail
from repositories.repository import mailRepository


def create_mail(db: Session, request: RequestMail):
    repository = mailRepository(db)
    return repository.create_mail(request.email.dict())

def get_mails(db: Session):
    repository = mailRepository(db)
    return repository.get_mails()

def get_mail_by_id(db: Session, id: int):
    repository = mailRepository(db)
    return repository.get_mail_by_id(id)

def update_mail(db: Session, id: int, request: RequestMail):
    repository = mailRepository(db)
    return repository.update_mail(id, request.email.dict())