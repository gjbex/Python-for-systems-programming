from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/users/{user_id}&{category}")
def read_item(user_id: int, category: str,
              q: Union[str, None] = None):
    return {"user_id": user_id, "category": category, "q": q}
