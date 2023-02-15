
 
#Pydantic
from pydantic import BaseModel
 
#FastAPI
from fastapi import FastAPI, HTTPException   
from fastapi import status
app = FastAPI()    


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    country: str
    age: int


users_list = [
    User(id=1,first_name="Miguel 1",last_name="Restrepo",country="Colombia",age="23"),
    User(id=2,first_name="Miguel 2",last_name="Restrepo",country="Colombia",age="23"),
    User(id=3,first_name="Miguel 3",last_name="Restrepo",country="Colombia",age="23")
    
    ]


@app.get(
    path="/users",
    status_code=status.HTTP_200_OK)
async def users():
    return users_list


#Path
@app.get(
    path="/user/{id}",
    status_code=status.HTTP_200_OK)
async def users(id:int):
    return search_user(id)

#Query
@app.get(
    path="/user/",
    status_code=status.HTTP_200_OK
    )
async def userquery(id: int):
    return search_user(id)

@app.post(
    path="/user/",
    status_code=status.HTTP_201_CREATED,
    response_model=User)
async def user(user: User):
    if type(search_user(user.id)) == User:
        HTTPException(status_code=404, detail="User already exists")
    else:
        users_list.append(user)

@app.put(
    path="/user/",
    status_code=status.HTTP_200_OK)
async def user(user:User):
    found = False
    for index ,saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        HTTPException(status_code=404, detail="User not exists")
    
@app.delete(
    path="/user/{id}",
    status_code=status.HTTP_200_OK)
async def user(id: int):
    found = False
    for index ,saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        HTTPException(status_code=404, detail="User not exists")





def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except :
        HTTPException(status_code=204, detail="hat ID don't was in the data")   
    

