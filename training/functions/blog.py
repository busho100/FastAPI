from .. import models
from .. schemas import Blog
from sqlalchemy.orm import Session

def get_all(db: Session):
    blogs =db.query(models.Blog).all()
    return blogs

def create(blog: Blog, db: Session):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog