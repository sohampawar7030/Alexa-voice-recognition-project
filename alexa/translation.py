import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound
import os

def alexa_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "").strip()
                print(command)
                return command
    except sr.UnknownValueError:
        print("Could not understand")
        return ""
    except sr.RequestError as e:
        print("Could not request result from Google: {0}".format(e))
        return ""

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Now")
    command = alexa_command()

if command:
    translator = Translator(to_lang="mr")  # Marathi language code
    try:
        translated_text = translator.translate(command)
        print(translated_text)
        
        # Generate speech from translated text
        tts = gTTS(text=translated_text, lang="mr")
        tts.save("translated_text.mp3")
        
        # Play the translated text
        playsound("translated_text.mp3")
        
        # Remove the temporary MP3 file
        os.remove("translated_text.mp3")
        
    except Exception as e:
        print("Error translating speech: {0}".format(e))
