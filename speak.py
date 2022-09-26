import pyttsx3                                  #import pytssx3 library for conversion of text to speech
import datetime

# speak function                         
def Say(Text):
    engine = pyttsx3.init("sapi5")               #sapi5 provides voice of man or woman for windows
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)    #select voice[0] from many voices
    engine.setProperty('rate' , 170)             #Rate at which Jarvis talk
    print("  ")
    print(f"Jarvis: {Text}")                     # Jarvis : (Text you write)
    engine.say(text = Text)                      #Jarvis speak text
    engine.runAndWait()
    print("  ")

def Wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        Say("good morning sir, your assistant is at your service. So, what are we doing today?")

    elif hour>12 and hour<18:
        Say("good afternoon sir, your assistant is at your service. So, what are we doing today?")

    else:
        Say("good evening sir, your assistant is at your service. So, what are we doing today?")

Wish()