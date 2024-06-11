import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from google_trans_new import google_translator


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def alexa_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
                return command
    except Exception as e:
        print(e)  
def run_alexa():
    while True:  # Keep the program running until manually stopped
        command = alexa_command()
        if command:
            if "play" in command:
                song = command.replace("play","")
                talk("Playing "+song)
                pywhatkit.playonyt(song)
            elif "time" in command:
                time = datetime.datetime.now().strftime("%I:%M %p")  # Changed to include AM/PM
                talk("The current time is "+time)
            elif "cricketer" in command:
                person = command.replace("cricketer", "").strip()
                info = wikipedia.summary(person, 5)
                talk(info)
            elif "search" in command:
                search_query = command.replace("search", "").strip()
                talk("Searching  "+search_query)
                info = wikipedia.summary(search_query, 5)
                talk(info)
            elif "stop" in command or "exit" in command:
                talk("Exiting the program")
                break
            else:
                talk("Sorry, I didn't understand that command.")


run_alexa()
