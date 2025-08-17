# 🤖 Jarvis - Your Personal AI Desktop Assistant

Jarvis is an advanced voice-controlled desktop assistant built with **Python**.
It can greet you, search the web, tell jokes, check weather, manage system tasks, and more!

---

## ✨ Features

* 🎙️ **Voice Commands** – Control using your voice (Speech Recognition).
* 👋 **Personal Greetings** – Jarvis introduces itself and greets you with time/day.
* 🌦️ **Weather Updates** – Get live weather information for any city.
* 🔋 **Battery Status** – Check your laptop’s current battery and charging status.
* 🎭 **Jokes & Fun** – Listen to jokes in English/Hindi.
* ⏰ **Timer** – Set custom timers with reminders.
* 🌐 **Internet Browsing** – Open YouTube, Google, GitHub, Chrome, etc.
* 📚 **Wikipedia Search** – Get summaries directly from Wikipedia.
* 🎶 **Music Player** – Play local songs from your system.
* 💻 **System Control** – Shutdown, restart, or open apps like VS Code, PyCharm.


---

## 🛠️ Tech Stack

* **Python 3.9+**
* `speechrecognition` – For voice input
* `pyttsx3` / `SAPI.SpVoice` – For text-to-speech (Windows voice)
* `psutil` – For system monitoring
* `requests` – For weather/news APIs
* `pyjokes` – For jokes
* `wikipedia` – For Wikipedia summaries


---

## 🚀 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/jarvis-assistant.git
   cd jarvis-assistant
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a file `config.py` (for API keys & email login):

   ```python
   WEATHER_API_KEY = "your-weather-api-key"
   EMAIL = "youremail@gmail.com"
   PASSWORD = "your-email-password"
   ```

---

## ▶️ Usage

Run the assistant:

```bash
python jarvis.py
```

Jarvis will:

* Greet you (e.g., *“Hello, I am Jarvis. Initializing systems now…”*)
* Wait for your command. Example commands:

  * **“Open YouTube”** → opens YouTube
  * **“Search Wikipedia for Python”** → gives wiki summary
  * **“Weather report”** → fetches live weather
  * **“Tell me a joke”** → says a random joke
  * **“Shut down”** → shuts down your PC

---

## 📸 Demo

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/605a1f91-2db3-4f9d-afce-ea954016217c" />

---

## 📌 To-Do / Future Features

* Add GUI interface with Jarvis face animation
* Integrate ChatGPT/Groq API for smart conversation
* Add reminder & calendar integration
* Cross-platform support (Linux/Mac)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---
