import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from random import choice
from utils import opening_text



USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

#s Set Volume
engine.setProperty('volume', 1.0)

# Set Voice 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)


# Text to Speech Conversion
def speak(text):
    '''
    Convert text to voice
    '''

    engine.say(text)
    engine.runAndWait()

def greet_user():
    '''
    Greet user according to the time
    '''
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f'Good morning {USERNAME}')
    elif (hour >= 12) and (hour < 16):
        speak(f'Good afternoon {USERNAME}')
    elif (hour >= 16) and (hour < 24):
        speak(f'Good evening {USERNAME}')
    
    speak(f'I am {BOTNAME}. How may I assist you?')

def take_user_input():
    '''
    Takes, user input, reconignzes it using Speech Recognition module and convert it into text
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = "en-US")
        print(query)
        if 'stop' in query or 'exit' in query:
            hour = datetime.now().hour
            if (hour >= 21) or (hour>=0 and hour<7):
                speak('Good night sir, take care!')
            else:
                speak('Have a good day sir!')
            exit()
        else:
            speak(choice(opening_text))

    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'none'
    return query
