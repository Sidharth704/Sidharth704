import speech_recognition as sr
import smtplib
from email.message import EmailMessage
import pyttsx3
from selenium import webdriver
engine=pyttsx3.init()
print('WELCOME TO HOME SERVER')
engine.say('welcome to home server')
engine.say('how can i help you')
engine.runAndWait()
print('1.KNOW THE BILLS')
print('2.CONTROL DEVICES')
print('3.NOTIFICATIONS')
print('notification is only available to android devices')
print('4.QUIT')
ch=int(input('enter your choice'))
if ch==1:
    listener = sr.Recognizer()
    engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('suryayavan@gmail.com', 'sidharth@2002')
    email = EmailMessage()
    email['From'] = 'suryayavan@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'bts': 'sayusidh@gmail.com',
    'pink': 'jennie@blackpink.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com'
}


def get_email_info():
    talk('what your name')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('say subject of your mail')
    subject = get_info()
    talk('say the content of your mail')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey, Your email is sent')
    


get_email_info()