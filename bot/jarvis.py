import pyttsx3 #pip install
import datetime #for importing date and time library
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
#import smtplib
#import webbrowser as wb

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    #Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 12 hour clock
    speak("The current time is")
    speak(Time)

#time_() uncomment this to use time_()

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

#date_() uncomment this to use date_()

def wishme():
    speak("Welcome back Reekraj Roy")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Jarvis at your service. Please tell me how can I help you today?")

#wishme()
def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio,language='en-US')
            print(query)

        except Exception as e:
            print(e)
            print("Say that again please.....")
            return "None"
        return query

'''
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls() #for this function, we must enable low security in gmail 

    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)

    server.close()
    '''

if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()     #all commands will be stored in lower case in query for easy recognition

        if 'time' in query: #tell us time when asked
            time_()

        elif 'date' in query: #tell us date when asked
            date_()

        elif 'wikipedia' in query:
            speak("Searching.....")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)
'''
        elif 'send email' in query:
            try:
                speak('What should I say?')
                content=TakeCommand()
                speak("Who is the receiver?")
                receiver=input("Enter Receiver's Email :")     #provide receiver's email
                to=receiver
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent')

            except Exception as e:
                print(e)
                speak("Unable to send Email.")

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = '/usr/bin/google-chrome%s'      
            #chromepath is location chrome's installation on computer

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')  #only open websites with '.com' at end
            '''