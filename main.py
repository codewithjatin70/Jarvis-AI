# ==========================
# 🤖 Jarvis - Python Desktop Assistant
# ==========================

# ---- Imports ----
import pyjokes
import time
import psutil
import requests
import smtplib
import os 
import webbrowser as web
import wikipedia as wiki
import speech_recognition as sr
import datetime as dt
import win32com.client as win

# ---- Text-to-Speech (Windows Voice API) ----
engine = win.Dispatch("SAPI.SpVoice")

def speak(audio):
    """Convert text to speech"""
    engine.Speak(audio)

# ---- Greeting Function ----
def WishMe():
    """Greets the user with time & day"""
    speak("Hello, I am Jarvis. Initializing systems now...")
    time.sleep(1)
    speak("System diagnostics complete. All systems are online.")
    time.sleep(1)
    
    # Get current hour & day
    hour = int(dt.datetime.now().hour)
    day = dt.datetime.now().strftime("%A")
    
    # Decide greeting
    if hour < 12:
        greet = "Good Morning"
    elif hour < 18:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"

    speak(f"{greet}, Today is {day}.")
    speak("Sir, tell me, how may I serve you today?")

# ---- Speech Recognition ----
def takeCommand():
    """Takes microphone input & converts it to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-hi-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# ---- Weather Report ----
def weather():
    """Fetch weather using WeatherAPI"""
    try:
        speak("Please tell me the city name")
        city = takeCommand().lower()
        url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            location = data["location"]["name"]
            region = data["location"]["region"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_kph = data["current"]["wind_kph"]

            report = f"Weather report for {location}, {region}, {country}: Temperature {temp_c}°C, Condition {condition}, Humidity {humidity}%, Wind {wind_kph} kph."
            print(report)
            speak(report)
        else:
            speak("Sorry, I couldn't fetch the weather report right now.")
    except Exception as a:
        print(a)
        speak("Sorry, something went wrong while fetching the weather.")

# ---- Battery Status ----
def batteryStatus():
    """Check system battery percentage & charging status"""
    try:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged
        status = "charging" if plugged else "not charging"

        message = f"Sir, the battery is at {percent}% and it's currently {status}."
        if not plugged and percent < 20:
            message += " Please plug in the charger soon."

        print(message)
        speak(message)
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't retrieve the battery status.")

# ---- Tell Jokes ----
def tellJoke():
    """Tell a random joke (fallback in Hindi if error)"""
    try:
        joke = pyjokes.get_joke(language="en", category="neutral")
        print(joke)
        speak(joke)
    except Exception as e:
        print(e)
        fallback_joke = "एक आदमी डॉक्टर के पास गया और बोला, डॉक्टर साहब मुझे भूलने की बीमारी हो गई है। डॉक्टर ने पूछा - कब से? आदमी बोला - कौन सी बीमारी?"
        speak(fallback_joke)

# ---- Shutdown & Restart ----
def shutdown():
    speak("Shutting down the system...")
    os.system('shutdown /s /t 1')

def restart():
    speak("Restarting the system...")
    os.system('shutdown /r /t 1')

# ---- Timer ----
def setTimer():
    """Set a timer in seconds"""
    try:
        speak("For how many seconds should I set the timer?")
        duration_str = takeCommand()
        if duration_str == "none":
            speak("Timer duration not recognized.")
            return

        duration = int(''.join(filter(str.isdigit, duration_str)))
        if duration <= 0:
            speak("Invalid time duration.")
            return

        speak(f"Timer set for {duration} seconds. Starting now.")
        while duration:
            if duration == 60:
                speak("1 minute left.")
            elif duration == 10:
                speak("10 seconds remaining.")
            elif duration <= 5:
                speak(str(duration))
            time.sleep(1)
            duration -= 1

        speak("Time's up! Wake up!")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't set the timer.")

# ======================
# MAIN PROGRAM START
# ======================
if __name__ == '__main__':
    WishMe()  # Greet user
    while True:
        query = takeCommand().lower()

        # Wikipedia Search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wiki.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open YouTube
        elif 'open youtube' in query:
            speak("Opening YouTube")
            web.open('youtube.com')

        # Exit Jarvis
        elif 'exit' in query or "band ho ja" in query:
            speak("Bye Bye Sir. Have a nice day!")
            break

        # Current Time
        elif 'the time' in query:
            time_now = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time_now}")
            print(f"Sir, the time is {time_now}")

        # Open Google
        elif 'open google' in query:
            speak("Opening Google")
            web.open("google.com")

        # Play Music
        elif 'play music' in query:
            music_dir = 'C:\\Users\\shiv\\Documents\\Music'
            songs = os.listdir(music_dir)
            speak("Starting Music")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        # Open VS Code
        elif 'open code' in query:
            codepath = 'C:\\Users\\shiv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            speak("Opening VS Code")
            os.startfile(codepath)

        # Open PyCharm
        elif 'open pycharm' in query:
            pycharm = 'C:\\Program Files\\JetBrains\\PyCharm 2025.1.1.1\\bin\\pycharm64.exe'
            speak("Opening PyCharm")
            os.startfile(pycharm)

        # Open GitHub Desktop
        elif "open github" in query:
            git = 'C:\\Users\\shiv\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
            speak("Opening GitHub Desktop")
            os.startfile(git)

        # Open Chrome
        elif "open chrome" in query:
            chrome = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            speak("Opening Chrome")
            os.startfile(chrome)

        # Weather Report
        elif 'weather' in query or 'weather report' in query:
            weather()

        # Battery Status
        elif 'battery status' in query:
            batteryStatus()

        # Jokes
        elif 'jokes' in query:
            tellJoke()

        # Shutdown
        elif 'shut down' in query:
            shutdown()

        # Restart
        elif 'restart' in query:
            restart()

        # Set Timer
        elif 'set the timer' in query:
            setTimer()

        else:
            speak("Oops! This information isn't available in my current dataset.")
