from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USERNAME = 'root'
DB_PASSWORD = 'ntuedtd'
DB_NAME = 'test'
DB_HOST_DOCKER = 'db:5432'
DB_HOST_LOCAL = 'localhost:5432'

# SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST_DOCKER}/{DB_NAME}"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST_LOCAL}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    