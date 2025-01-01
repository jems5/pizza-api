from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]
    
    class Config:
        from_attribute = True
        json_schema_extra = {
            'example':{
                "username": "john",
                "email": "john@gmail.com",
                "password": "12345",
                "is_active": True,
                "is_staff": False 
            }
        }
        

class Settings(BaseModel):
    authjwt_secret_key:str='55a80fcdec94179d5d8576afa9fe8ae314fc6b6591e64e1f1103b410efbf1731'
        
class LoginModel(BaseModel):
    username: str
    password: str