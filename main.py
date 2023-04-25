from fastapi import FastAPI, Depends

from database import get_db
from user.routes import user_router

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(user_router)
