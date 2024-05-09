import httpx

async def fetchAllMovies():
    url = "https://api.nomoreparties.co/beatfilm-movies"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()