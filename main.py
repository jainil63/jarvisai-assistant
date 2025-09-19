import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
import cv2
import requests
import webbrowser
import wikipedia
import random

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)

def speak(audio):
    engine.say(audio)
    print(f"Jarvis: {audio}")
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
    except Exception as e:
        speak("Say again please...")
        return "none"
    return query.lower()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!!")
    else:
        speak("Good evening sir!!")
    speak("I am Jarvis, please tell me how can I help you!!")

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand()

        # Open Notepad
        if "open notepad" in query:
            speak("Opening notepad")
            os.startfile("C:\\Windows\\System32\\notepad.exe")

        # Open Chrome and Search
        elif "open chrome" in query:
            speak("What should I search on chrome?")
            search = takecommand()
            webbrowser.open(f"https://www.google.com/search?q={search}")

        # Wikipedia Search
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except:
                speak("Sorry sir, I could not find anything on Wikipedia.")

        # Open YouTube
        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Tell Time
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")

        # Tell Date
        elif "date" in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Sir, today's date is {date}")

        # Play Music
        elif "play music" in query:
            music_dir = "D:\\Music"  # <-- change this to your music folder
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                speak(f"Playing {song}")
                os.startfile(os.path.join(music_dir, song))
            else:
                speak("No songs found in the music folder.")

        # Open Camera
        elif "open camera" in query:
            speak("Opening the camera.")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                if not ret:
                    break
                cv2.imshow("Webcam", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()

        # Get IP Address
        elif "ip address" in query:
            ip = requests.get("https://api.ipify.org").text
            speak(f"Your IP address is {ip}")

        # Save Notes
        elif "make a note" in query:
            speak("What should I write sir?")
            note = takecommand()
            with open("jarvis_notes.txt", "a") as f:
                f.write(f"{datetime.datetime.now()} : {note}\n")
            speak("Note saved successfully.")

        elif "read notes" in query:
            try:
                with open("jarvis_notes.txt", "r") as f:
                    notes = f.read()
                speak("Here are your notes.")
                print(notes)
                speak(notes)
            except:
                speak("You have no saved notes.")

        # Quit
        elif "quit jarvis" in query or "sleep" in query or "bye" in query:
            speak("Goodbye sir, take care!")
            sys.exit(0)