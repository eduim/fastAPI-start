from pydantic import BaseModel

class User(BaseModel):
  id: int 
  name: str

class Input(BaseModel):
  id: int | None = None
  name: str  

class Place(BaseModel): 
  id: int
  name: str
  description: str
  price: int

class PlaceInput(BaseModel):
  name: str
  description: str
  price: int


users = {
  1: User(id=1, name="John Doe"),
  2: User(id=2, name="Adam Smith"),
  3: User(id=3, name="Aja Iim")
}

places = {
  
}