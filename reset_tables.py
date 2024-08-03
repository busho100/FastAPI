from sqlalchemy import create_engine
from training.models import Base
from training.database import engine

# テーブルを削除する
Base.metadata.drop_all(bind=engine)

# テーブルを再作成する
#Base.metadata.create_all(bind=engine)
