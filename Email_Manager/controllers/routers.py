#routee
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.schemas import RequestMail, Response,mailSchema
from controllers import crud


router = APIRouter()

@router.post('/create')
async def create_mail(request: RequestMail, db: Session = Depends(get_db)):
    created_mail = crud.create_mail(db, request)
    return Response(email = created_mail).dict(exclude_none = True)

@router.get('/')
async def get_mails(db: Session = Depends(get_db)):
    mails = crud.get_mails(db)
    return Response(email = mails).dict(exclude_none = True)

@router.get('/{id}')
async def get_mail_by_id(id: int, db: Session = Depends(get_db)):
    mail = crud.get_mail_by_id(db, id)
    return Response(email = mail).dict(exclude_none=True)

@router.put('/put/{id}')
async def update_mail(request: RequestMail, id: int, db: Session = Depends(get_db)):
    updated_mail = crud.update_mail(db, id, request)
    return Response(email = updated_mail).dict(exclude_none = True)