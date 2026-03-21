from fastapi import APIRouter, Depends, HTTPException 
from ..models import UpdateUser
from ..databasemodels import get_db
from sqlalchemy import Session
from . import models
import bcrypt 
from auth import get_active_user

router = APIRouter()
@router.put('/user/update')
def update(request: UpdateUser, current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == current_user.id).first()
  user.name = request.name
  user.email = request.email
  password = request.password.encode("UTF-8")
  new_password = bcrypt.hashpw(password , bcrypt.gensalt())
  user.password = new_password
  db.commit()
  db.refresh(user)
  return user
