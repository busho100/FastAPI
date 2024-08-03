from fastapi import FastAPI, Depends
from training.schemas import Blog
from training.models import Base, Blog as BlogModel
from training import models
from training.database import engine, sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get('/blog_get')
def all_fetch(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog_get/{id}')
def show(id:int,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog


@app.post('/blog')
def create(blog:Blog, db: Session= Depends(get_db)):
    new_blog = BlogModel(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

