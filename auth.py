from fastapi import APIRouter,status, Depends
from schema import SignUpModel, LoginModel
from database import db_connection, Session
from model import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

engine = db_connection()
session = Session(bind=engine)

auth_router = APIRouter(
    prefix= "/auth",
    tags = ['auth']
)

@auth_router.post("/signup", response_model=SignUpModel, status_code = status.HTTP_201_CREATED)
async def signup(user:SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    
    if db_email is not None:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
                             detail = "Email taken"
                             )
    
    db_username = session.query(User).filter(User.username == user.username).first()
    
    if db_username is not None:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
                             detail = "Username taken"
                             )
    
    new_user = User(
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_active = user.is_active,
        is_staff = user.is_staff
    )
    
    session.add(new_user)
    
    session.commit()
    
    return new_user
        

#login

@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user:LoginModel, Authorize:AuthJWT=Depends()):
    db_user = session.query(User).filter(User.username == user.username).first()
    check_password = check_password_hash(db_user.password, user.password)
    
    if db_user and check_password:
        access_token = Authorize.create_access_token(subject=db_user.username)
        refresh_token = Authorize.create_refresh_token(subject=db_user.username)
        response = {
            "access": access_token,
            "refresh": refresh_token
        }
        
        return jsonable_encoder(response)
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, details="Invalid Login Credentials")
