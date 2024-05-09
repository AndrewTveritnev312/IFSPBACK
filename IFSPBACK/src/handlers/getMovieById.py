import httpx

async def fetchMovieById(movie_id: int):
    url = f"https://api.nomoreparties.co/beatfilm-movies/{movie_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()