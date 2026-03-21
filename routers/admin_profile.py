from fastapi import APIRouter, Depends HTTPException
from . import models 
from ,.models import User 
from ..databasemodels import get_db
from sqlalchemy import Session

router = APIRouter()
@router.get('/user/admin_profile')

def get_users(current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  if current_user.role != "admin":
    raise HTTPException(status_code=403, detail="permission denied")
  users = db.query(models.User).all()
  return users
