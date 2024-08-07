from fastapi import FastAPI, Depends, status, Response, HTTPException
from training.schemas import Blog, ShowBlog, User, ShowUser
from training.models import Base, Blog as BlogModel
from training.hashing import Hash
from training import models
from training.database import engine, sessionLocal, reset_database
from typing import List
from sqlalchemy.orm import Session


app = FastAPI()

#reset_database()

Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get('/blog_get', response_model=List[Blog], tags=['blogs'])
def all_fetch(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# @app.get('/blog_get/{id}', status_code=status.HTTP_200_OK)
# def show(id:int, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return{'detail':f'Blog with the id{id} is not available'}

#     return blog

@app.get('/blog_get/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs']) 
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id{id} is not avaiable')

    return blog




@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(blog:Blog, db: Session= Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog_get/{id}',status_code = status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise 
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()

    return 'Deletion completed'

@app.put('/blog_get/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: Blog, db: Session=Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog_query.first():
        raise 
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog_query.update(request.dict(),synchronize_session=False)
    db.commit()

    return{'Update completed'}


@app.post('/user', status_code=status.HTTP_201_CREATED, tags=['users'])
def create_user(request: User, db:Session = Depends(get_db)):
    #パスワードのハッシュ化
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}', response_model=ShowUser, tags=['users'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id{id}is not available')
    
    return user