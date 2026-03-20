from fastapi import APIRouter, Depends, HTTPException 
from . import models 
from ..models import User
from auth import get_active_user
from ..databasemodels import get_db

router = APIRouter()

@router.get('/user/me')
def get_user(current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == current_user.id).first()
  if not user:
    raise HTTPException(status_code=404, detail="user not found")
  return {
    "name": current_user.name,
    "email": current_user.email,
    "message": "welcome to your profile"
  }
