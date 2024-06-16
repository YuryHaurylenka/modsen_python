import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI
from pathlib import Path

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv()

CORRECT_API_KEY = os.getenv('CORRECT_API_KEY')
WRONG_API_KEY = 'incorrect_api_key'
app = FastAPI()


@app.get("/all-statuses")
async def get_all_statuses():
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    test_cases = [
        {"params": {"q": "London", "appid": CORRECT_API_KEY}, "description": "Correct API key and city name"},
        {"params": {"q": "London", "appid": WRONG_API_KEY}, "description": "Incorrect API key"},
        {"params": {"appid": CORRECT_API_KEY}, "description": "Missing city name"},
        {"params": {"q": "NonExistentCity", "appid": CORRECT_API_KEY}, "description": "Non-existent city"},
        {"params": {"lat": "invalid_latitude", "lon": "invalid_longitude", "appid": CORRECT_API_KEY},
         "description": "Invalid coordinates"}
    ]

    statuses = []

    async with httpx.AsyncClient() as client:
        for case in test_cases:
            try:
                response = await client.get(base_url, params=case["params"])
                statuses.append({
                    "description": case["description"],
                    "status_code": response.status_code,
                    "response_body": response.json()
                })
            except httpx.HTTPStatusError as exc:
                statuses.append({
                    "description": case["description"],
                    "status_code": exc.response.status_code,
                    "response_body": exc.response.text
                })

    return statuses
