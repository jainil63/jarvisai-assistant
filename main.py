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
engine.setProperty('voice', voices[1].id)

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
    except Exception:
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

# ---- System Control Functions ----
def shutdown():
    speak("Shutting down the system.")
    os.system("shutdown /s /t 1")

def restart():
    speak("Restarting the system.")
    os.system("shutdown /r /t 1")

def sleep_pc():
    speak("Putting the system to sleep.")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand()

        # ---- New Commands ----
        if "shutdown" in query:
            shutdown()

        elif "restart" in query:
            restart()

        elif "sleep" in query:
            sleep_pc()

        # Quit
        elif "quit jarvis" in query or "bye" in query:
            speak("Goodbye sir, take care!")
            sys.exit(0)

