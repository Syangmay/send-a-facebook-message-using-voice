import time
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
def talk(audio):
    engine = pyttsx3.init()
    print(audio)
    engine.say(audio)
    engine.runAndWait()
def myCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source , duration = 1)
        audio= r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said " + command + "\n")
    except sr.UnknownValueError:
        command = myCommand()
    return command
def Facebook_Message():
    talk("Who is the recipeint")
    text1 = myCommand()
    talk(text1)
    talk("What is the message")
    text2 = myCommand()
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome('E:/chromedriver' ,options = options )
    driver.maximize_window()
    driver.get('https://www.facebook.com/')
    email = driver.find_element_by_id('email')
    email.send_keys('your email') # enter your email
    password = driver.find_element_by_id('pass')
    password.send_keys('************') #replace ******** with your password
    button = driver.find_element_by_id('u_0_2')
    button.click()
    search = driver.find_element_by_class_name('_58al')
    
    search.send_keys(text1)
    time.sleep(15)
    search1 = driver.find_element_by_class_name('_58al')
    search1.send_keys(Keys.ENTER)
    time.sleep(3)
    message = driver.find_element_by_css_selector('div.notranslate._5rpu')
    
    message.send_keys(text2)
    message1 = driver.find_element_by_css_selector('div.notranslate._5rpu')
    message1.send_keys(Keys.ENTER)
    talk("Message is sent")

Facebook_Message()