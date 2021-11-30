from fastapi import APIRouter, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends

from app import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import  models, utils, oauth2

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model=schemas.Token)
def login(user_credentails: OAuth2PasswordRequestForm =Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentails.username).first()
    print(user_credentails)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'User with this email does not exists')

    if not utils.verify(user_credentails.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')


    access_token = oauth2.create_access_token(data = {"user_id": user.id})

    return {"access_token":access_token, "token_type": "bearer"}
