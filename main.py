import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[-1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def main():
    speak("Hello i am jarvis")


if __name__ == "__main__":
    main()
