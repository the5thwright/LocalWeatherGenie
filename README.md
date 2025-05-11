# LocalWeatherGenie

**Version 1.0 (v1.0) — Your Local, Private, AI-Powered Weather Bot**

---

## 🌦️ What is LocalWeatherGenie?

LocalWeatherGenie is a beginner-friendly, privacy-first weather bot that:
- Fetches real-time weather data for any city using [WeatherAPI](https://www.weatherapi.com/)
- Uses a local large language model (Mistral via [Ollama](https://ollama.com/)) to generate friendly, natural-language weather reports
- Runs entirely on your computer — no cloud LLMs, no data leaks, no OpenAI
- Logs all actions and errors for easy troubleshooting

---

## ✨ Features
- **Local AI**: All language generation is done on your machine (Mistral via Ollama)
- **Real Weather**: Uses WeatherAPI for up-to-date forecasts
- **Beginner Friendly**: Step-by-step setup, no prior Python or AI experience needed
- **Extensible**: Easy to add new features, locations, or even chat with Mistral
- **Robust Logging**: All actions and errors are logged to `changelog.txt`

---

## 🚀 Quick Start

### 1. **Prerequisites**
- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Ollama](https://ollama.com/) (for local LLM)
- A free [WeatherAPI key](https://www.weatherapi.com/)

### 2. **Clone the Repo**
```sh
git clone https://github.com/the5thwright/LocalWeatherGenie.git
cd LocalWeatherGenie
```

### 3. **Set Up Python Environment**
```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 4. **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 5. **Install Ollama and the Mistral Model**
- Download and install Ollama from [https://ollama.com/](https://ollama.com/)
- Open a terminal and run:
  ```sh
  ollama pull mistral
  ollama run mistral
  ```
  This will download and start the Mistral model locally.
- **Alternative (Hugging Face):** If you want to use a different model, see [Ollama's docs](https://ollama.com/library) or [Hugging Face](https://huggingface.co/models) for compatible models.

### 6. **Get a WeatherAPI Key**
- Sign up at [https://www.weatherapi.com/](https://www.weatherapi.com/)
- Copy your API key
- Open `weather_bot.py` and replace `YOUR_WEATHERAPI_KEY_HERE` with your key

### 7. **Run the Bot!**
```sh
python weather_bot.py
```
- Enter a location (e.g., `Marion, IN` or `London`) when prompted
- Get a friendly, AI-generated weather report

---

## 🛠️ Troubleshooting
- **Ollama not running/model not found:**
  - Make sure you ran `ollama run mistral` in a separate terminal
  - The script will check and tell you if Ollama or the model is missing
- **WeatherAPI 502 or quota errors:**
  - Wait and try again (API outages are common on free plans)
  - Check your API key and quota at [WeatherAPI dashboard](https://www.weatherapi.com/my/)
- **Python errors:**
  - Make sure you activated your virtual environment and installed dependencies
- **See `changelog.txt`** for detailed logs of all actions and errors

---

## 🧩 Extending LocalWeatherGenie
- **Change the prompt**: Edit the `prompt` in `generate_report()` for different report styles
- **Add chat mode**: Use the same Ollama API to build a chat tool (see [Ollama API docs](https://github.com/jmorganca/ollama/blob/main/docs/api.md))
- **Schedule reports**: Use Windows Task Scheduler or `cron` to run the script automatically
- **Send reports by email/SMS**: Integrate with `smtplib` or Twilio
- **Add a GUI**: Use `tkinter` or another Python GUI library

---

## 📝 Example Output
```
Enter a location (e.g., 'Marion, IN' or 'London'): Marion, IN
Good morning Marion! It's going to be a lovely day today with clear skies and high temperatures reaching 76 degrees. Sunrise is at 6:28 AM and sunset will be around 8:47 PM. The average humidity will be about 71%, so it should feel comfortable outside. And great news, there's no chance of rain today! Enjoy your day!
```

---

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.

---

## 🏷️ Version
**LocalWeatherGenie v1.0 (Mark One)**

---

## 💡 Inspiration & Credits
- [Ollama](https://ollama.com/) for local LLM serving
- [WeatherAPI](https://www.weatherapi.com/) for weather data
- [Mistral](https://mistral.ai/) for the open-source LLM
- [Hugging Face](https://huggingface.co/) for model hosting

---

**Questions or suggestions? Open an issue or PR!**
