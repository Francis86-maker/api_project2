from fastapi import APIRouter, Depends, HTTPException 
from ..databasemodels import get_db
from ..models import Items,User
from . import models
from sqlalchemy import Session
from auth import get_active_user

router = APIRouter()
@router.get('/user/search')
def items(request: Items, current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  item = db.query(models.Items).filter(models.Items.name == request.name).first()
  if not item:
    raise HTTPException(status_code=404, detail="item not found")
  if current_user.id != owner_id and current_user.role == "admin":
    raise HTTPException(status_code=403, detail="permission denied")
  return item
