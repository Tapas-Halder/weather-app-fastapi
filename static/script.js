const form = document.getElementById("searchForm");
const cityInput = document.getElementById("cityInput");
const message = document.getElementById("message");
const card = document.getElementById("weatherCard");

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    await getWeather();
});

async function getWeather() {
    const city = cityInput.value.trim();

    if (!city) {
        message.textContent = "Please enter a city name.";
        card.classList.add("hidden");
        return;
    }

    message.textContent = "Searching...";
    card.classList.add("hidden");

    try {
        // Call our FastAPI backend.
        // Relative URL works both locally and on Render.
        const response = await fetch(
            "/weather?city=" + encodeURIComponent(city)
        );

        const data = await response.json();

        if (!response.ok || data.error) {
            message.textContent = data.error || "Something went wrong.";
            return;
        }

        document.getElementById("city").textContent =
            data.city + ", " + data.country;

        document.getElementById("temperature").textContent =
            data.temperature + "°C";

        document.getElementById("weather").textContent =
            data.weather;

        document.getElementById("feelsLike").textContent =
            data.feels_like;

        document.getElementById("humidity").textContent =
            data.humidity;

        document.getElementById("wind").textContent =
            data.wind_speed;

        document.getElementById("weatherIcon").src =
            "https://openweathermap.org/img/wn/" + data.icon + "@2x.png";

        message.textContent = "";
        card.classList.remove("hidden");

    } catch (error) {
        message.textContent = "Could not connect to the weather server.";
    }
}
