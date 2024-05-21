#schem.py
from typing import  Optional,Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import datetime
from typing import List

T = TypeVar('T')
class mailSchema(BaseModel):
    email_from:Optional[str] = None
    email_to:Optional[str] = None
    subject :Optional[str] = None
    content : Optional[str] = None
    status:Optional[str] = None
    create_at:Optional[datetime] = None
   
    class Config:
        orm_mode = True 

class RequestMail(BaseModel):
    email: mailSchema  = Field(...)

class Response (GenericModel,Generic[T]):
    email: Optional[T]