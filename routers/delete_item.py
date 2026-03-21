from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy import Session 
from ..databasemodels import get_db
from ..models import Items
from . import models 
from auth import get_active_user

router = APIRouter()

def delete_item(request: Items, current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  item_to_delete = db.query(models.Items).filter(models.Items.name = request.name).first()
  if not item_to_delete:
    raise HTTPException(status_code=404, detail="item not found")
  if current_user.role =="admin" and current_user.id != owner_id:
    raise HTTPException(status_code=400, detail="not cheating")
  db.delete(item_to_delete)
  db.commit()
  return {
    "message": "done"
  }
  
