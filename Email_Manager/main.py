from fastapi import FastAPI
from model.model import Base
from database.db import engine
from controllers.routers import router 


app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get('/')
async def Home(): 
    return " Home "

app.include_router(router, prefix="/emails", tags=["Emails"])