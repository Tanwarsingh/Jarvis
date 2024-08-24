import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
import webbrowser
import smtplib
import sys
import time
import pyjokes
from bs4 import BeautifulSoup
import numpy as np
import urllib.request



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold= 1    
            audio = r.listen(source,timeout=1,phrase_time_limit=10)

    try:
         print("recognizing...")
         qurey = r.recognize_google(audio, language="en-in")
         print(f"user said:{qurey}")        
     
    except Exception as e:
         speak (" say that again please")
         return "none"
    return qurey     

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
         speak(f" good morning, it's {tt}")

    elif hour>12 and hour<18:
         speak(f"good afternoon, it's {tt}")

    else:
         speak(f"good evening, it's {tt}")
    speak(" i am friday sir , how may i help you")

# to email
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('bsranawat7841@gmail.com','Bugs@54321')
    server.sendmail('bsranawat7841@gmail.com',to,content)
    server.close()

if __name__=='__main__':
    wish()
    while True:
    
        query = takecommand().lower()

         #logic building for task

        if "open notepad" in query:
           npath = "C:\\Windows\\system32\\notepad.exe"
           os.startfile(npath)

        elif"command prompt" in query:
             os.system("start cmd")
             
        elif"open camera" in query:
            cap = cv2.VideoCapture(0)
            while True :
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif"play music" in query:
             music_dir ="C:\\Users\\bsran\Music\\New folder"
             songs = os.listdir(music_dir)
             rd = random.choice(songs)
             os.startfile(os.path.join(music_dir,rd))

        elif"ip address" in query:
             ip = requests('http://api.ipify.org').text
             speak(f"your ip address is {ip}")

        elif"open youtube" in query:
          webbrowser.open("www.youtube.com")

        elif"open facebook" in query:
          webbrowser.open("www.facebook.com")

        elif"open google" in query:
          speak("sir, what should i search ")
          cm = takecommand().lower()
          webbrowser.open(f"{cm}")

        elif"are you up" in query:
          speak("for you , i am always up")

        elif"Close YouTube" in query:             
            speak("okay sir, closing youtube")
            os.system("taskkill /im chrome.exe /f")
        
        elif"how are you" in query:
            speak("I am always good as you and availble for you")

        elif"email to yash" in query:
            try:
                speak("what should i say sir")
                content=  takecommand().lower()
                to = "bugs1012004@gmail.com"
                sendEmail(to,content)
                speak(" email has been sent to nikita ")

            except Exception as e:
                print(e)
                speak(" sorry sir, i am not able to send this email")

        elif"no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()
        
        elif"temperature" in query:
            search = "temperature in chittorgarh"
            url = f"http://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif"open mobile camera" in query:
            URL = "http://100.79.187.192.8080/shot.jpg" 
            while True:
                img_arr= np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q = cv2.waitKey(1)
                if q==ord("q"):
                    break;

            cv2.destroyAllWindows()        



# to close any application
        elif"close notepad "in query:
            speak("okay sir , closing notepad")
            os.system("taslkill/f/im notepad.exe")
        elif"close command" in query:
            speak("okay sir , closing command promt")
            os.system("taslkill/f/im cmd.exe ")
# to set an alarm 

        elif"set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==5:
                music_dir= "C:\\Users\\bsran\Music\\New folder"
                songs= os.listdir(music_dir)    
                os.startfile(os.path.join(music_dir, songs[0]))

# to finbd the joke
        elif"tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif" shutdown the system" in query:
            os.system("shutdown/s/t s")

        elif " restart the system" in query:
            os.system("shutdown/r/t s")
            
             
        elif"sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0.1.0")


        speak("sir, do you have any other work")


