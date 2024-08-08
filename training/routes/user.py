from fastapi import APIRouter, Depends, status, HTTPException
from ..schemas import User, ShowUser
from ..database import get_db
from .. import models
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter()

@router.post('/user', status_code=status.HTTP_201_CREATED, tags=['users'])
def create_user(request: User, db:Session = Depends(get_db)):
    #パスワードのハッシュ化
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=ShowUser, tags=['users'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id{id}is not available')
    
    return user