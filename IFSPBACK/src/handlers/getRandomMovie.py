import httpx
import random
async def fetchRandomMovies():
    random_integer = random.randint(1, 100)
    url = f"https://api.nomoreparties.co/beatfilm-movies/{random_integer}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()