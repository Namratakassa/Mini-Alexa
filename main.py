
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print("Initializing Alexa")

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[0])
 
 # speak function will speak rather pronounce the string which is pass to it

def speak(text):
    engine.say(text)
    engine.runAndWait()

# this function will wish you as per the current time..
def wishMe():


    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
          speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Alexa. How may i help you?")

# this function will take command from microphone    
def takeCommand():




    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehol()
    server.starttls()
    server.login('youremai@gmail.com', 'password')
    server.sendmail("namrata.kassa@mmit.edu.in", to, content)
    server.close()

# Main program starts here.....
def main():

    speak("Initializing Alexa...")
    wishMe()
    query = takeCommand()

    # logic for executing task as per the query
    if query:
        if 'wikipedia' in query.lower():
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)


    if 'open youtube' in query.lower():
        # webbrowser.open("youtube.com")
        url = "youtube.com"

        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Prnav Kassa\\Downloads"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    elif 'open code' in query in lower():
        codePath = "C:\\Users\\Prnav Kassa\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(codePath)

    elif 'email to namrata' in query.lower():
        try:
            speak("What should I send")
            content = takecommand()
            to = "namrata@gamail.com"
            sendmail(to, content)
            speak("Email has been sent successfully")

        except Exception as e:
            print(e)

main()