from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Weather App API")

# Allow the frontend to call our FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


@app.get("/")
def home():
    # Show our HTML website
    return FileResponse("static/index.html")


@app.get("/weather")
async def get_weather(city: str = Query(..., min_length=1)):
    if not OPENWEATHER_API_KEY:
        return {"error": "OPENWEATHER_API_KEY is missing"}

    # OpenWeather API URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code != 200:
        return {"error": "City not found"}

    data = response.json()

    # Send only the data our website needs
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
    }
