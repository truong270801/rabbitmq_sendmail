#model.py
from sqlalchemy import Column ,Integer, String, TIMESTAMP

from database.db import Base

class Mail(Base):
    __tablename__ = "emails"

    id = Column(Integer,primary_key=True,autoincrement=True)
    email_from = Column(String)
    email_to = Column(String)
    subject = Column(String)
    content = Column(String)
    status = Column(String)
    create_at = Column(TIMESTAMP)
