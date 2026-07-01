from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app=FastAPI()
movies=[{
    "id":1,
    "title":"Inception",
    "genre":"Sci-Fi",
    "rating":8.8
    },
    {
        "id":2,
        "title":"The Dark Knight",
        "genre":"Action",
        "rating":9.0
    }]
class Movie(BaseModel):
    title:str
    genre:str
    rating:float

class MovieUpdate(BaseModel):
    title:Optional[str]=None
    genre:Optional[str]=None
    rating:Optional[float]=None

@app.get("/")
def home():
    return {"message": "Welcome to the Movie Management API!"}

@app.get("/movies")
def get_movies(genre:str=None):
    if genre:
        filtered_movies=[]
        for m in movies:
            if m["genre"].lower()==genre.lower():
                filtered_movies.append(m)
        return filtered_movies
    return  movies


