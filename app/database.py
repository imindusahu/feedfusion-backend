from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "mysql+pymysql://smart_user:1234@localhost/smart_aggregator"

# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()