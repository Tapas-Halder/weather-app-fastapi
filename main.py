from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Weather App API")

# Frontend can call our FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Make CSS and JavaScript available
app.mount("/static", StaticFiles(directory="static"), name="static")

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


@app.get("/")
def home():
    # Show the website
    return FileResponse("static/index.html")


@app.get("/weather")
async def get_weather(city: str = Query(..., min_length=1)):
    if not OPENWEATHER_API_KEY:
        return {"error": "OpenWeather API key is missing"}

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
    }

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url, params=params)

        if response.status_code != 200:
            return {"error": "City not found"}

        data = response.json()

        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"],
        }

    except Exception:
        return {"error": "Weather service is temporarily unavailable"}
