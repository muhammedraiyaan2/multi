# this is multi package
import os
import random
import webbrowser
import pyjokes
import pyttsx3
import time
import wikipedia
import datetime
def add(a,b):
    """This function add two numbers"""
    return a+b
def sub(a,b):
    """This function subract two number"""
    return a-b
def mul(a,b):
    """This function multiply two numbers"""
    return a*b
def div(a,b):
    """This function divide two numbers"""
    return a/b
def avg(a,b):
    """This function will be the average number of two number"""
    return (a+b)/2
def speak(text):
    """This function speak the text that you have given in the arrgument
    Note: You have install this pyttsx3 package for sound. copy the command and paste in the terminal
    command: pip install pyttsx3"""
    engine=pyttsx3.init('sapi5')
    voices= engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    engine.say(text)
    engine.runAndWait()
    return text
def sleep(seconds):
    """This function will sleep with the given seconds like time.sleeo() function"""
    time.sleep(seconds)
def random_choice(var_name):
    """This function work like random.choice() function"""
    return random.choice(var_name)
def random_num(range_start,range_end):
    """This function return the random number that you have given in the arrguments. It works like random.randint() function"""
    return random.randint(range_start,range_end)
def open(url):
    """This function open the url that you have given. It works like webbrowser.open() function"""
    webbrowser.open(url)
def open_chrome(url,chrome_path):
    """This function will open website in chrome you have to first give the url and second you have to give the chorme path
    Note: the path must be like example D:\\coding\\chomre.exe you have to use the double backslash not single backslash"""
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)
def out(*args):
    """This function prints the value that you want to print"""
    print(*args)
def send(value):
    """This function return the value"""
    return value
def get_joke():
    """This function return a random joke
    Note: You have to install a package called pyjokes. Paste the command in the terminal
    Command: pip install pyjokes"""
    return pyjokes.get_joke()
def wikipedia_search(result,sentence):
    """This function search in wikipedia and get the results and return it to you.
    Note: you have to install wikipedia package. copy the command and paste it to your terminal.
    command: pip install wikipedia"""
    result = wikipedia.summary(result,sentences=sentence)
    return result
def get_time():
    """This function will return you time with hour minutes and seconds"""
    return datetime.datetime.now().strftime("%H")+":"+datetime.datetime.now().strftime("%M")+":"+datetime.datetime.now().strftime("%S")
def open_program(path):
    """This function will open the program or the folder that you wanted to be open.
    Note: the path must be like example D:\\coding\\multi.py you have to use the double backslash not single backslash"""
    os.startfile(path)

def remove(path):
    """This function will remove the program that you want to remove
    Note: the path must be like example D:\\coding\\multi.py you have to use the double backslash not single backslash"""
    os.remove(path)
def lists(path):
    """This function will return the list of the folder and files"""
    return os.listdir(path)
def inp(text):
    """This function will take the input from user and you have to give the text in the function"""
    input(text)
