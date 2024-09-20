import speech_recognition as sr
import pyttsx3
import sys
import subprocess

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        command = None
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        command = None
    return command

def main():
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        if command:
            if "exit" in command.lower() or "quit" in command.lower():
                speak("Goodbye!")
                break
            elif "hello" in command.lower():
                speak("Hello! How are you?")
            elif "tells about you" in command.lower():
                speak("I'm just a computer program, so I don't have feelings, but thank you for asking!")
            else:
                speak("Sorry, I don't know how to respond to that.")

if __name__ == "__main__":
    # Check for distutils
    try:
        import distutils
    except ModuleNotFoundError:
        print("distutils is not available, installing setuptools may fix this.")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools"])
        except Exception as e:
            print(f"Error upgrading setuptools: {e}")
    main()
