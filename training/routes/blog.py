from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..schemas import Blog, ShowBlog, ShowUser, User
from ..database import get_db
from .. import models
from sqlalchemy.orm import Session

router = APIRouter()



@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(blog:Blog, db: Session= Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog_get/{id}',status_code = status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise 
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()

    return 'Deletion completed'

@router.put('/blog_get/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: Blog, db: Session=Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog_query.first():
        raise 
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog_query.update(request.dict(),synchronize_session=False)
    db.commit()

    return{'Update completed'}

@router.get('/blog_get', response_model = List[ShowBlog], tags=['blogs'])
def all_fetch(db: Session = Depends(get_db)):
    blogs =db.query(models.Blog).all()

    return blogs

@router.get('/blog_get/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs']) 
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id{id} is not avaiable')

    return blog
