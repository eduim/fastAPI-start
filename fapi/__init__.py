from fastapi import FastAPI, HTTPException, Response
from fapi.data import users, places, User, Input, Place, PlaceInput

app = FastAPI()

@app.get('/')
def index():
  return {'message': 'Hello World!'}

@app.get('/users')
def get_users() -> list[User]:
  return list(users.values())

@app.post('/users')
def create_user(user: Input) -> User: 
  id = getId(users)
  users[id] = User(id=id, name=user.name)
  return users[id]

@app.get('/places')
def get_places() -> list[Place]:
  return list(places.values())

@app.get('/places/{place_id}')
def get_place(place_id: int) -> Response: 
  if place_id not in places:
    return HTTPException(status_code=404, detail="Place not found")
  else:
    return places[place_id]
    
@app.post('/places')
def create_place(place: PlaceInput) -> Response:
  if place.name == None or place.description == None or place.price == None:
    return HTTPException(status_code=400, detail="Invalid input")
  
  id = getId(places)

  places[id] = Place(id=id, name=place.name, description=place.description, price=place.price)
  return places[id]

@app.put('/places/{place_id}')
def update_place(place_id: int, place: PlaceInput) -> Response:
  if place.name == None or place.description == None or place.price == None:
    return HTTPException(status_code=400, detail="Invalid input")
  
  if place_id not in places:
    return HTTPException(status_code=404, detail="Place not found")
  else:
    places[place_id] = Place(id=place_id, name=place.name, description=place.description, price=place.price)
    return places[place_id]


@app.delete('/places/{place_id}')
def delete_place(place_id: int) -> Response: 
  if place_id not in places:
    return HTTPException(status_code=404, detail="Place not found")
  else:
    del places[place_id]
    return Response(status_code=204)

def getId(dict): 
  if not dict: 
    return 0
  else: 
    return max(dict.keys()) + 1