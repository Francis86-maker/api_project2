from fastapi import APIRouter , Depends, HTTPException 
from sqlalchemy import Session
from . import models 
from ..databasemodels import get_db
from ..models import User
import bcrypt

router = APIRouter()

@router.post('/user')
def create_user(request: User, db: Session=Depends(get_db)):
  existing_email = db.query(models.User).filter(models.User.email == request.email).first()
  if existing_email:
    raise HTTPException(status_code=400, detail="email already exists")
  password = request.password.encode("UTF-8")
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  new_user = models.User(name = request.name, email = request.email, password = hashed)
  db.add(new_user)
  db.commit()
  db.refresh(new_usee)
  return {
    "name": new_user.name,
    "email": new_user.email
  }
  
  
