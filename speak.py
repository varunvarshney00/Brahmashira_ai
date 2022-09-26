import pyttsx3
import datetime

# speak function
def Say(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)      #to change the voice 
    engine.setProperty('rate', 170)
    print("     ")      #blank line
    print(f"Brahmashira: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("     ")      #blank line

def Wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        Say("good morning sir, your assistant is at your service.")

    elif hour>12 and hour<18:
        Say("good afternoon sir, your assistant is at your service.")

    else:
        Say("good evening sir, your assistant is at your service.")

Wish()