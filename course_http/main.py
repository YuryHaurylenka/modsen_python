import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

CORRECT_API_KEY = os.getenv("CORRECT_API_KEY")
WRONG_API_KEY = "incorrect_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

app = FastAPI()


@app.get("/statuses")
async def get_all_statuses():
    """
    Get all statuses from OpenWeather API
    """
    test_cases = [
        {"params": {"q": "London", "appid": CORRECT_API_KEY}, "description": "Correct API key and city name"},
        {"params": {"q": "London", "appid": WRONG_API_KEY}, "description": "Incorrect API key"},
        {"params": {"appid": CORRECT_API_KEY}, "description": "Missing city name"},
        {"params": {"q": "IncorrectCity", "appid": CORRECT_API_KEY}, "description": "Incorrect city"},
        {"params": {"lat": "invalid_latitude", "lon": "invalid_longitude", "appid": CORRECT_API_KEY},
         "description": "Invalid coordinates"},
        {"params": {"lat": 0, "lon": 0, "appid": CORRECT_API_KEY},
         "description": "Valid coordinates for lattitude and longitude"},
        {"params": {"q": "Minsk", "appid": CORRECT_API_KEY},
         "description": "Correct API key and another valid city name"},
        {"params": {"q": "", "appid": CORRECT_API_KEY}, "description": "Empty city name"},
        {"params": {"q": "12345", "appid": CORRECT_API_KEY}, "description": "City name with numbers"}
    ]

    statuses = []

    async with httpx.AsyncClient() as client:
        for case in test_cases:
            try:
                response = await client.get(BASE_URL, params=case["params"])
                statuses.append({
                    "description": case["description"],
                    "status_code": response.status_code,
                    "response_body": response.json()
                })
            except httpx.RequestError:
                statuses.append({
                    "description": case["description"],
                    "status_code": response.status_code,
                    "response_body": response.json()
                })
            except httpx.HTTPStatusError:
                statuses.append({
                    "description": case["description"],
                    "status_code": response.status_code,
                    "response_body": response.json()
                })

    return {"statuses": statuses}


@app.get("/weather/{city}")
async def get_weather_city(city: str):
    """
    Get weather for city.
    """
    params = {"q": city, "appid": CORRECT_API_KEY, "units": "metric"}

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        weather_data = response.json()

    return {
        "city": city,
        "temperature": weather_data["main"]["temp"],
        "weather": weather_data["weather"][0]["description"].title(),
        "humidity": weather_data["main"]["humidity"],
        "wind_speed": weather_data["wind"]["speed"]
    }
