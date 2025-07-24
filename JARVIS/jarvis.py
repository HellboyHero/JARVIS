
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

#text to speech...
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text...
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again sir please")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    # tt = time.strftime("%I : %M %p")
    
    if hour>=0 and hour<=12:
        speak("good morning")

    if hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    
    speak("hello sir i am jarvis.  please tell how can i help you")

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.login('deadlydealer0786@gmail.com', 'Sohail@1230786')
#     server.sendmail('deadlydealer0786@gmail.com', to , content)
#     server.close()
    
if __name__ == "__main__":
    # takecommand()
    wish()
    while True:
    # if 1:
        query = takecommand().lower()

    #logic building for the tasks
        if "open notepad" in query:
            npath = "C:\\Users\\MD AYAAN SOHAIL\\OneDrive\\Desktop\\JARVIS\\notes.txt"
            os.startfile(npath)

        if "wikipedia" in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 5)
            speak("According to wikipedia")
            speak(result)
        
        elif "open command prompt" in query:
            os.system("start cmd")
         
        elif "open camera" in query:
            # cv2.namedWindow("preview")
            # vc = cv2.VideoCapture(0)
            # #cap = cv2.videoCapture(0)
            # while True:
            #     ret, img = vc.read()
            #     cv2.imshow('webcam', img)
            #     k = cv2.waitKey(50)
            #     if k == 27:
            #         break;
            # vc.release()
            # cv2.destroyAllWindows("preview")
            cv2.namedWindow("preview")
            vc = cv2.VideoCapture(0)

            if vc.isOpened(): # try to get the first frame
                rval, frame = vc.read()
            else:
                rval = False

            while rval:
                cv2.imshow("preview", frame)
                rval, frame = vc.read()
                key = cv2.waitKey(20)
                if key == 27: # exit on ESC
                    break

            vc.release()
            cv2.destroyWindow("preview")


        elif "play music" in query:
            music_dir = "C:\\Users\\MD AYAAN SOHAIL\\OneDrive\\Desktop\\JARVIS\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir , rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'settings' in query:
            speak('opening settings of ur computer')
            os.system("Settings")

        elif "send message" in query:
            kit.sendwhatmsg("+918179210207", "this is Ayaan",14,20)
            time.sleep(100)
            speak("msg has been sent")

        elif "play songs on youtube" in query:
            kit.playonyt("say something")

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        # elif "email to ram" in query:
        #     try:
        #         speak("what should i say?")
        #         content = takecommand().lower()
        #         to = "deadlydealer0786@gmail.com"
        #         sendEmail(to, content)
        #         speak("email has been sent to ram")

        #     except Exception as e:
        #         print(e)
        #         speak("sorry sir , i cannot send this email to ayaan")

        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
        # speak("sir, do u have any other work!!")

# to close an application
        elif "close notepad" in query:
            speak("okey sir, closing the notepad")
            os.system("taskkill /f /im notes.txt")


# to set an alarm 
        elif " set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==24:
                music_dir = "C:\\Users\\MD AYAAN SOHAIL\\OneDrive\\Desktop\\JARVIS\\songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[2]))
# to tell jokes
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t S")

        elif "restart the system" in query:
            os.system("shutdown /r /t S")

# to switch windows
        elif "switch windows" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("alt")
            time.sleep(1)
            pyautogui.keyUp("alt")

# to take screenshot:
        elif "take screenshot" in query or "take screenshot" in query:
            speak("sir,Please tell me the name for the screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshots")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir,the screenshot is saved in our main folder.now i am ready for your next")

         

