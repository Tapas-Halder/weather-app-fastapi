async function getWeather() {
    const city = document.getElementById("cityInput").value.trim();
    const message = document.getElementById("message");
    const card = document.getElementById("weatherCard");

    if (!city) {
        message.textContent = "Please enter a city name.";
        card.classList.add("hidden");
        return;
    }

    message.textContent = "Loading...";
    card.classList.add("hidden");

    try {
        // JavaScript calls our FastAPI backend
        const response = await fetch(
            "http://127.0.0.1:8000/weather?city=" + encodeURIComponent(city)
        );

        const data = await response.json();

        if (data.error) {
            message.textContent = data.error;
            return;
        }

        document.getElementById("city").textContent =
            data.city + ", " + data.country;

        document.getElementById("weather").textContent =
            data.weather;

        document.getElementById("temperature").textContent =
            data.temperature + "°C";

        document.getElementById("feelsLike").textContent =
            data.feels_like;

        document.getElementById("humidity").textContent =
            data.humidity;

        document.getElementById("wind").textContent =
            data.wind_speed;

        message.textContent = "";
        card.classList.remove("hidden");

    } catch (error) {
        message.textContent = "Could not connect to FastAPI.";
    }
}
