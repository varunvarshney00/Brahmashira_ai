import speech_recognition as sr         #import speech recognition for converting speech to text by recognizing the speech

def Listen():                           # use the default microphone as the audio source
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source , 0 , 4)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = "en-in")    # listen for the first phrase and extract it into query data
        print(f"You said : {query}")                             # You said : (text you speak)
    except: 
        return ""
    
    query = str(query)                                           # Retrun the text in the form of string having lowercase letters
    return query.lower()