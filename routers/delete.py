from fastapi import APIRouter, Depends, HTTPException 
from auth import get_admin_permission
from . import models 
from ..models import User 
from ..databasemodels import get_db
from sqlalchemy import Session

router = APIRouter()
@router.delete('/delete')
def delete_user(current_user: User=Depends(get_admin_permission), db: Session=Depends(get_db)):
  admin_count = db.query(models.User).filter(models.User.role == "admin").count()
  user_to_delete = db.query(models.User).filter(models.User.id == request.id).first()
  if admin_count <= 1 and user_to_delete.role == "admin":
    raise HTTPException(status_code=400, detail=" cannot have ome admin")
  db.delete(user_to_delete)
  db.commit()
  return {
    "message": "user deleted"
  }
  
