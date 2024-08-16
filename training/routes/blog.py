from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..schemas import Blog, ShowBlog, ShowUser, User
from ..database import get_db
from .. import models
from sqlalchemy.orm import Session
from ..functions import blog

router = APIRouter(
    prefix='/blog',
    tags = ['blogs']
)



@router.post('/', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(blog:Blog, db: Session= Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id, db: Session = Depends(get_db)):
    
    return blog.destroy(id, db)

@router.put('{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog, db: Session=Depends(get_db)):

    return blog.update(id, request, db)

@router.get('/', response_model = List[ShowBlog], tags=['blogs'])
def all_fetch(db: Session = Depends(get_db)):
    blogs =db.query(models.Blog).all()

    return blogs

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs']) 
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id{id} is not avaiable')

    return blog
