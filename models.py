from pydantic import BaseModel 

class User(BaseModel):
  name: str
  email: str
  password: str
class Item(BaseModel):
  name: str
  price: int
  description: str
class UpdateItem(BaseModel):
  name: str
  price: int
  description: str
class UpdateUser(BaseModel):
  name: str
  email: str
  password: str
