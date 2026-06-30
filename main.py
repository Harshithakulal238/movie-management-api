from fastapi import FastAPI
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
@app.get("/")
def home():
    return {"message": "Welcome to the Movie Management API!"}

@app.get("/movies")
def get_movies():
    return  movies

@app.get("/movies/{id}")
def get_movie(id: int):
    for m in movies:
        if m["id"]==id:
            return m
    return {"message":"Movie not found"}