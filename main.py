import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()  # text to speech
voices = engine.getProperty('voices')  # get voice types
voices = engine.setProperty('voice', voices[1].id)  # set the alexa voice type


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    # try-catch will prevent crash while checking for audio input source
    try:
        with sr.Microphone() as source:
            print('Listening...Speak now.')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('clara', '')
            else:
                talk('Please say \"Clara\", before speaking command')
    except:
        pass
    return command


def run_alexa():
    try:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)  # song will play on YouTube automatically
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('The current time is ' + time)  # tells the current time
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)  # Find information on a person
        elif 'what is' in command:
            something = command.replace('who is', '')
            info = wikipedia.summary(something, 2)
            print(info)
            talk(info)  # Find information on event or thing
        elif 'date' in command:
            talk('Sorry, I\'m not interested, but we can be friends though')
        elif 'are you single' in command:
            talk('Sorry, I\'m already in a relationship with Chat GPT')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('I\'m sorry, I didn\'t quite get that. Could you please say it again')
    except:
        pass


# Re-run function if Alexa fails to understand command
while True:
    run_alexa()
