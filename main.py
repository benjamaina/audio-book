"""
This script uses the pyttsx3 library for text-to-speech conversion and the speech_recognition library to recognize speech from the microphone.
Functions:
    speak(text):
        Converts the given text to speech and plays it through the speakers.
        Args:
            text (str): The text to be converted to speech.
    takeCommand():
        Listens to the user's speech through the microphone, recognizes it using Google's speech recognition service, and returns the recognized text.
        Returns:
            str: The recognized text from the user's speech. Returns "None" if the speech could not be recognized or if there was an issue with the recognition service.
Usage:
    When the script is run, it prompts the user to say something, recognizes the speech, and prints the recognized text.
"""
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please say that again.")
        speak("Sorry, I didn't catch that. Please say that again.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("There was an issue with the recognition service. Please try again.")
        return "None"
    return query

if __name__ == "__main__":
    print("Say something to test:")
    user_query = takeCommand()
    print(f"You said: {user_query}")
   