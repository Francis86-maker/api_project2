from fastapi import APIRouter, Depends, HTTPException 
from fastapi.security import oauth2 
from ..databasemodels import get_db
from jose import jwt
ALGORITHM="HS256"
SECRET_KEY = "francissecret"
oauth2_scheme = oauth2PasswordBearer(Login_URL="Login")

def get_active_user(token: str=Depends(oauth2_scheme), db: Session=Depends(get_db)):
  payload = jwt.decode(algorithms=["HS256"], token, SECRET_KEY)
  user_id = payload.get("user_id")
  user = db.query(models.User).filter(models.User.id == user_id).first()
  if not user:
    raise HTTPException(status=404, detail="not found")
  return user

def get_admin_permission(current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  if current_user.role != "admin":
    raise HTTPException(status_code=403, detail="not accepted")
  return {
    "message": "done"
  }
