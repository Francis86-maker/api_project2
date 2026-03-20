from ..databasemodels import get_db
from fastapi import APIRouter, Depends, HTTPException 
from . import models 
from ..models import User
import bcrypt
from jose import jwt
from datetime import datetime , deltatime 

router = APIRouter()

@router.post('/login')
def Login(request: User, db: Session=Depends(get_db)):
  user = db.query(models.User).filter(models.User.email == request.email).first()
  if not user:
    raise HTTPException(status_code=404, detail="email not found")
  password = request.password.encode("UTF-8")
  valid_password = bcrypt.checkpw(password, user.password)
  if not valid_password:
    raise HTTPException(status_codd=404, detail="wrong password")
  token_data = {
    "user_id": user_id,
    "role": user.role,
    "exp": datetime.utcnow() + deltatime(hours=12)
  }
  token = jwt.encode(token_data, algorithm="HS256", SECRET_KEY)
  return {
    "message": "user logged in successfully"
  }
