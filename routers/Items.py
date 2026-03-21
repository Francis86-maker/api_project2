from fastapi import APIRouter, Depends, HTTPException 
from ..models import Items
from ..databasemodels import get_db
from . import models 

router = APIRouter()

@router.post('/items')
def create_item(request: Items, db: Session=Depends(get_db)):
  new_item = models.Items(name = request.name, price = request.price, description= request.description).first()
  db.add(new_item)
  db.commit()
  db.refresh(new_item)
  return {
    "name": new_item.name,
    "price": new_item.price,
    "description": new_item.description
  }
