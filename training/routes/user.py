from fastapi import APIRouter, Depends, status, HTTPException
from ..schemas import User, ShowUser
from ..database import get_db
from sqlalchemy.orm import Session
from ..functions import users

router = APIRouter(
    prefix='/user',
    tags=['users']
)

@router.post('/')
def create_user(request: User, db:Session = Depends(get_db)):
    #パスワードのハッシュ化
    
    return users.create(request, db)

@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    
    return users.show(id, db)