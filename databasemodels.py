from sqlalchemy import String , Integer, Column , ForeignKey
from database import declarative_base
from sqlalchemy.orm import relationship , sessionmaker

engine = create_engine("sqlite///:blog.db", echo=True)
SessionLocal = sessionmaker(auto_commit=False, auto_Flush=False, bind=engine)

Base = declarative_base()

class User(Base):
  __tablename__ = "Users"
  id = Column(Integer, primary_key=True, unique=True)
  name = Column(String)
  email = Column(String)
  password = Column(String)
  role = Column(String, default="user")
  owner_id = Column(Integer, ForeignKey="Items.id")
  items = relationship("Item", back_populates="creator")
class Item(Base):
  __tablename__ ="Items"
  id = Column(Integer, primary_key=True, unique=True)
  name = Column(String)
  price = Column(String)
  description= Column(String)
  user_id = Column(Integer, ForeignKey="Users.id")
  creator = relationship("User", back_populates="items")

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


