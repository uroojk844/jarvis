import speech_recognition as sr
import pyttsx3
import pyautogui
import time

def listen() -> str:
    """Listens to the microphone and returns transcribed text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing speech...")
            text = recognizer.recognize_google(audio)  # type: ignore
            return text
        except sr.UnknownValueError:
            return ""  # Unrecognized speech
        except (sr.RequestError, Exception):
            return ""


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def load_prompt(name):
    with open(f"prompts/{name}.md", "r", encoding="utf-8") as f:
        return f.read()

def highlight():
    pyautogui.press("ctrl")
    pyautogui.press("ctrl")
    time.sleep(0.5)
    pyautogui.press("ctrl")
    pyautogui.press("ctrl")