import sys
from click import command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
bot = pyttsx3.init()
voices = bot.getProperty("voices")
bot.setProperty("voice", voices[1].id)


def respond(text):
    bot.say(text)
    bot.runAndWait()


def getcommand():
    try:
        with sr.Microphone() as mic:
            print("Speak anything ")
            voice = listener.listen(mic)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command


def run():
    respond("What you would like me to do Ash ?")
    command = getcommand()
    if "play" in command:
        searchtext = command.replace("play", "")
        print(command)
        respond("Playing" + searchtext)
        pywhatkit.playonyt(searchtext)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%p")
        respond("Current time is" + time)
    elif "who is" in command:
        query = command.replace("who is", "")
        info = wikipedia.summary(query, sentences=2)
        print(info)
        respond(info)
    elif "what is" in command:
        query = command.replace("what is", "")
        info = wikipedia.summary(query, sentences=2)
        print(info)
        respond(info)
    elif "joke" in command:
        respond(pyjokes.get_joke())
    elif "bye" in command:
        respond("Okay bye bye")
        sys.exit()

    respond("Do you want me to do anything else ?")
    command = getcommand()
    if "yes" in command:
        run()
    elif "no" in command:
        respond("Okay, bye bye")
        sys.exit()


while True:
    run()
