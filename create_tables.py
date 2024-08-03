from sqlalchemy import create_engine
from training.models import Base
from training.database import engine

# テーブルを作成する
Base.metadata.create_all(bind=engine)
