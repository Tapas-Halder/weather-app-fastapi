# 🌤️ Weather App FastAPI

A simple full-stack weather application for learning.

## Technologies

- HTML
- CSS
- JavaScript
- FastAPI
- OpenWeather API
- Python

## Project flow

Frontend → FastAPI → OpenWeather API → FastAPI → Frontend

## Run locally

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install packages

```bash
pip install -r requirements.txt
```

### 4. Create .env

Create a file named `.env` in the project root:

```env
OPENWEATHER_API_KEY=your_real_api_key
```

Never upload `.env` to GitHub.

### 5. Start FastAPI

```bash
uvicorn main:app --reload
```

### 6. Open the frontend

Open `static/index.html` in your browser.

Enter a city such as:

- Kolkata
- Tokyo
- Delhi
- London

## API

```
GET /weather?city=Kolkata
```
