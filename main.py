from fastapi import FastAPI
from orders import order_router
from auth import auth_router
from database import db_connection
from fastapi_jwt_auth import AuthJWT
from schema import Settings

app = FastAPI()

@app.get("/")
async def hello():
    db_connection()
    return{"hello world"}

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(order_router)
app.include_router(auth_router)
