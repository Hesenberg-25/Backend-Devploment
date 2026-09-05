from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# This defines which SQL we are using like here we are using SQLLite but we can also use PostGre or even MySql

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
# engine is the Bridge between the Backend and the Database where we are telling that we are using SQLLite
# And check_same_thread is a Marker to tell Backend like only one Request at a TIME will be handled as SQLLite is Single Thread

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal is a Machine which created WorkSpace (Instances) where the User is helped to create a Post and when the Post is Created the WorkSapce is Destroyed
# And for new Post again a new Session will start

class Base(DeclarativeBase):
    pass


def get_db():
    with SessionLocal() as db:
        yield db