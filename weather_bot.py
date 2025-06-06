import os
import requests
import datetime
from urllib.parse import quote_plus  # <-- Added for URL encoding

# No OpenAI imports or API keys needed

# Weather API key (still required for weather data)
WEATHER_API_KEY = "b30d599df20f4b3abc6113928251105"
OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "mistral"

# --- Logging ---
def log_action(message):
    """Log actions and errors to changelog.txt with a timestamp."""
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open("changelog.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")

# --- Ollama Health Check ---
def check_ollama_health():
    """Check if Ollama is running and the required model is available."""
    log_action("Checking Ollama health...")
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        response.raise_for_status()
        tags = response.json().get("models", [])
        if not any(OLLAMA_MODEL in (tag.get("name", "") or "") for tag in tags):
            log_action(f"Model '{OLLAMA_MODEL}' not found in Ollama. Available: {[t.get('name') for t in tags]}")
            raise RuntimeError(f"Model '{OLLAMA_MODEL}' not found in Ollama. Please run: ollama run {OLLAMA_MODEL}")
        log_action("Ollama health check passed.")
    except Exception as e:
        log_action(f"Ollama health check failed: {e}")
        raise RuntimeError(f"Ollama health check failed: {e}") from e

# --- Weather Data Fetching ---
def get_weather(location="Marion, IN"):
    """Fetch weather data for the given location using WeatherAPI."""
    encoded_location = quote_plus(location)
    log_action(f"Fetching weather for '{location}' (encoded: '{encoded_location}')...")
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={encoded_location}&days=1&aqi=yes"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        try:
            data = res.json()
        except Exception as e:
            log_action(f"Weather API returned non-JSON response: {res.text[:200]}")
            raise RuntimeError(f"Weather API did not return valid JSON. Response: {res.text[:200]}") from e
    except requests.exceptions.RequestException as e:
        log_action(f"Weather API request failed: {e}")
        raise RuntimeError(f"Weather API request failed: {e}") from e

    if "forecast" not in data or not data["forecast"].get("forecastday"):
        log_action(f"Weather API response missing forecast data: {data}")
        raise RuntimeError(f"Weather API response missing forecast data: {data}")

    forecast = data["forecast"]["forecastday"][0]["day"]
    astro = data["forecast"]["forecastday"][0]["astro"]

    log_action(f"Weather data fetched successfully for {location}.")
    return {
        "location": location,
        "condition": forecast["condition"]["text"],
        "max_temp": forecast["maxtemp_f"],
        "min_temp": forecast["mintemp_f"],
        "sunrise": astro["sunrise"],
        "sunset": astro["sunset"],
        "humidity": forecast["avghumidity"],
        "chance_of_rain": forecast["daily_chance_of_rain"]
    }

# --- LLM Report Generation using Ollama (Mistral) ---
def generate_report(location):
    """Generate a friendly weather report for the given location using Ollama (Mistral)."""
    weather = get_weather(location)
    prompt = f"""Today's weather report for {weather['location']}:
- Condition: {weather['condition']}
- High: {weather['max_temp']}°F, Low: {weather['min_temp']}°F
- Sunrise: {weather['sunrise']}, Sunset: {weather['sunset']}
- Average Humidity: {weather['humidity']}%
- Chance of Rain: {weather['chance_of_rain']}%
\nCreate a short, friendly verbal weather update from this data:"""
    log_action("Sending prompt to Ollama for generation...")
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        result = response.json()
        log_action("Ollama LLM generation successful.")
        return result["response"]
    except Exception as e:
        log_action(f"Ollama LLM request failed: {e}")
        raise RuntimeError(f"Ollama LLM request failed: {e}") from e

# --- Main Entry Point ---
if __name__ == "__main__":
    try:
        check_ollama_health()
        # Prompt the user for their location
        user_location = input("Enter a location (e.g., 'Marion, IN' or 'London') [default: Marion, IN]: ").strip()
        if not user_location:
            user_location = "Marion, IN"
        print(generate_report(user_location))
    except Exception as e:
        print(f"Error: {e}")
        log_action(f"Script failed: {e}")
