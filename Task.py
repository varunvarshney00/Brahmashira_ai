import imp
import datetime
from speak import Say
import os
import cv2
import random
from requests import get
import webbrowser
import requests
from bs4 import BeautifulSoup

# FUNCTION

# 2TYPES

# 1 - NON INPUT
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def Notepad():
    npath = "C:\\windows\\system32\\notepad.exe"
    os.startfile(npath)

def Cmd():
    os.system("start cmd")

def Camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(50)
        if k==27:
            break
        cap.release()
        cv2.destroyAllWindows()

def Music():
    music_dir = "E:\\Jarvis"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    for song in songs:
        if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, song))

def Ip():
    ip = get("https://api.ipify.org").text
    Say(f"Your ip address is {ip}")

def Youtube():
    webbrowser.open("www.youtube.com")

def Weather():
    searching = "temperature in bangalore"
    url = f"https://www.google.com/search?q={searching}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    Say(f"current {searching} is {temp}")

def Google():
    webbrowser.open("www.google.com")


def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()
    
    elif "day" in query:
        Day()

    elif "notepad" in query:
        Notepad()

    elif "command prompt" in query:
        Cmd()

    elif "camera" in query:
        Camera()

    elif "music" in query:
        Music()

    elif "ip" in query:
        Ip()

    elif "youtube" in query:
        Youtube()

    elif "google" in query:
        Google()

    elif "temperature" in query:
        Weather()
    

# 2 - INPUT

def InputExecution(tag, query):
    if "wikipedia" in tag:
        Say("Searching wikipedia..")
        name = str(query).replace("who is","").replace("about", "").replace("tell me about","").replace("what is the", "").replace("wikipedia", "").replace("can you explain about", "").replace("explain", "").replace("tell me more", "")
        import wikipedia
        result = wikipedia.summary(name)
        Say("according to wikipedia")
        Say(result)

    # elif "google" in tag:
    #     query = str(query).replace("google","")
    #     query = query.replace("search","")
    #     import pywhatkit
    #     pywhatkit.search(query)