from fastapi import APIRouter, Depends, HTTPException 
from ..models import UpdateItem, User
from ..databasemodels import get_db
from . import models
from auth import get_active_user
from sqlalchemy import Session

router = APIRouter()
@router.put('/user/items_update')
def update_item(request: UpdateItem, current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  item = db.query(models.Items).filter(models.Items.owner_id == current_user.id).first()
  if not item and current_user.role == "admin":
    raise HTTPException(status_code=400, detail="doesn't match permission rules")
  item.name = request.name
  item.price = request.price
  item.description = request.description
  db.commit()
  db.refresh(item)
  return item
