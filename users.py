from fastapi import FastAPI
from pydantic import BaseModel
    
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


@app.get("/users")
async def users():
    return users_list


#Path
@app.get("/user/{id}")
async def users(id:int):
    return search_user(id)

#Query
@app.get("/user/")
async def userquery(id:int):
    return search_user(id)



def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except :
        return  "That ID don't was in the data"   
    