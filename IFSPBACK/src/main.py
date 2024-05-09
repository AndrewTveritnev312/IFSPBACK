from fastapi import FastAPI
from handlers.getMovieById import fetchMovieById
from handlers.getAllMovies import fetchAllMovies
from handlers.getRandomMovie import fetchRandomMovies


app = FastAPI()


@app.get("/movie/{movie_id}")
async def getMovieById(movie_id: int):
    movie_data = await fetchMovieById(movie_id)
    return movie_data


@app.get("/movies")
async def getAllMovies():
    all_movies_data = await fetchAllMovies()
    return all_movies_data


@app.get("/movies/getRandom")
async def getRandomMovie():
    random_movie_data = await fetchRandomMovies()
    return random_movie_data

origins = [
    "http://http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

