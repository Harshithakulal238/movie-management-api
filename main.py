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


@app.get("/movies/{id}")
def get_movie(id:int):
    for m in movies:
        if m["id"]==id:
            return m
    return {"error":"Movie not found"}

@app.get("/movies")
def get_movies(genre:str=None):
    if genre:
        filtered_movies=[]
        for m in movies:
            if m["genre"].lower()==genre.lower():
                filtered_movies.append(m)
        return filtered_movies
    return  movies

@app.post("/movies")
def create_movie(movie:Movie):
    movie_dict=movie.model_dump()
    movie_dict["id"]=len(movies)+1
    movies.append(movie_dict)
    return movie_dict

@app.put("/movies/{id}")
def update_movie(id:int,updated_movie:Movie):
    for i,m in enumerate(movies):
        if m["id"]==id:
            movie_data=updated_movie.model_dump()
            movie_data["id"]=id
            movies[i]=movie_data
            return movie_data
    return {"message":"Movie not found"}
