from fastapi import APIRouter, Depends, HTTPException 
from ..models import Items
from ..databasemodels import get_db
from . import models 
from auth import get_active_user

router = APIRouter()

@router.post('/items')
def create_item(request: Items,current_user: User=Depends(get_active_user),  db: Session=Depends(get_db)):
  new_item = models.Items(name = request.name, price = request.price, description= request.description,owner_id = current_user.id).first()
  db.add(new_item)
  db.commit()
  db.refresh(new_item)
  return {
    "name": new_item.name,
    "price": new_item.price,
    "description": new_item.description
  }
