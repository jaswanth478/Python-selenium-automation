import time
import requests
import pyttsx3
import pyautogui as p
from collections import defaultdict
from selenium import webdriver
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

dic = { "wifi": "https://internet.lpu.in", 'whatsapp': "https://web.whatsapp.com", 'leave': 'https:/ums.lpu.in/lpuums',
       'flight': "https://www.google.com/travel/flights?tfs=CBwQARoJagcIARIDREVMQAFIAXABggELCP___________wGYAQI&tfu=KgIIAw"}


def wedb():
    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\Hp\\AppData\\Local\\Microsoft\\Edge\\User Data")
    service = Service("C:/ms.exe")
    driver = webdriver.Edge(service=service, options=options)
    """
    service = Service(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    options = Options()
    driver = webdriver.Edge(service=service, options=options)"""
    return driver


def msg(k, nunber="1234"):
    d = wedb()
    d.get(dic["whatsapp"])
    d.maximize_window()
    time.sleep(5)
    cursor = d.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    cursor.click()
    cursor.send_keys(nunber)
    cursor.send_keys(Keys.RETURN)
    time.sleep(2)
    p.click(x=1400, y=1000)
    p.write(k)
    p.hotkey("enter")
    time.sleep(1)

    return 0


def recive(n):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            speek("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=20)
            text = r.recognize_google(audio)
            return text.lower()


        except sr.exceptions.UnknownValueError:
            if n == 3:
                return
            recive(n + 1)
        except sr.RequestError as e:
            speek("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.WaitTimeoutError:
            speek("Timeout: No speech detected within 5 seconds")


def speek(s):
    k = pyttsx3.init()
    k.say(s)
    k.runAndWait()


def incheck():
    try:
        requests.get(url="https://internet.lpu.in", timeout=2)
        return 1

    except (requests.ConnectionError, requests.Timeout) as exception:

        d = wedb()
        d.get(dic["wifi"])
        time.sleep(10)
        cursor = d.find_element(By.XPATH, ' /html/body/form/div/table/tbody/tr/td/div[1]/div/div[1]/div[3]/input')
        cursor.click()
        cursor = d.find_element(By.XPATH, '/html/body/form/div/table/tbody/tr/td/div[1]/div/div[2]/div[2]/input')
        cursor.click()
        cursor.send_keys("2222")#id to connect to lpu hostels or school wifi
        cursor = d.find_element(By.XPATH, '/html/body/form/div/table/tbody/tr/td/div[1]/div/div[2]/div[3]/input')
        cursor.click()
        cursor.send_keys("2222")#password
        cursor = d.find_element(By.XPATH, '//*[@id="jsena"]/table/tbody/tr/td/div[1]/div/div[2]/div[5]')
        cursor.click()
        speek("connected to wifi")
        return 0


def checkin():
    try:
        request = requests.get(url="https://amazon.in", timeout=5)
        return request

    except (requests.ConnectionError, requests.Timeout) as exception:
        if incheck():
            speek("connected")
        else:
            speek("connect lpu network")
            return 0


def leave():
    d = wedb()
    d.get(dic["leave"])
    d.maximize_window()
    d.get('https://ums.lpu.in/lpuums')

    cursor = d.find_element(By.XPATH, '//*[@id="txtU"]')
    cursor.click()
    time.sleep(5)
    cursor = d.find_element(By.XPATH, '//*[@id="txtU"]')
    cursor.click()
    cursor.send_keys("123456")#lpu registration
    cursor.send_keys(Keys.TAB)
    time.sleep(2)
    cursor = d.find_element(By.NAME, 'TxtpwdAutoId_8767')
    cursor.click()
    cursor = d.find_element(By.NAME, 'TxtpwdAutoId_8767')
    cursor.click()
    cursor.send_keys("123456")#password

    cursor.send_keys(Keys.ENTER)
    d.get('https://ums.lpu.in/lpuums/frmStudentHostelLeaveApplicationTermWise.aspx')
    cursor = d.find_element(By.NAME, 'ctl00$cphHeading$ddlLeaveTerm')
    cursor.send_keys(Keys.ARROW_DOWN)
    cursor = d.find_element(By.NAME, 'ctl00$cphHeading$ddlLeaveTerm')
    cursor.send_keys(Keys.ARROW_DOWN)
    cursor = d.find_element(By.NAME, 'ctl00$cphHeading$drpLeaveType')
    cursor.send_keys(Keys.ARROW_DOWN)
    cursor = d.find_element(By.NAME, 'ctl00$cphHeading$drpLeaveType')
    cursor.send_keys(Keys.ARROW_DOWN)
    cursor = d.find_element(By.NAME, 'ctl00$cphHeading$ddlVisitDay')
    cursor.send_keys('LL')
    cursor = d.find_element(By.ID, 'ctl00_cphHeading_startdateRadDateTimePicker1_timePopupLink')
    cursor.click()
    cursor = d.find_element(By.XPATH, '//*[@id="ctl00_cphHeading_startdateRadDateTimePicker1_timeView_tdl"]/tbody'
                                      '/tr[10]/td[4]/a')
    cursor.click()
    cursor = d.find_element(By.ID, 'ctl00_cphHeading_enddateRadDateTimePicker2_timePopupLink')
    cursor.click()
    d.find_element(By.XPATH,
                   '//*[@id="ctl00_cphHeading_enddateRadDateTimePicker2_timeView_tdl"]/tbody/tr[10]/td[5]/a').click()
    d.find_element(By.NAME, 'ctl00$cphHeading$txtLeaveReason').send_keys("reason")
    time.sleep(200)


def flight(fm, to):
    d = wedb()
    d.get(dic['flight'])
    time.sleep(2)
    cursor = d.find_element(By.XPATH, '//*[@id="i21"]/div[1]/div/div/div[1]/div/div/input')
    cursor.click()
    time.sleep(1)
    cursor = d.find_element(By.XPATH, '//*[@id="i21"]/div[6]/div[2]/div[2]/div[1]/div/input')
    print("here")
    cursor.send_keys(fm)
    time.sleep(2)
    cursor.send_keys(Keys.ARROW_DOWN)
    cursor.send_keys(Keys.ARROW_DOWN)
    cursor.send_keys(Keys.RETURN)
    time.sleep(2)
    cursor = d.find_element(By.XPATH, '//*[@id="i21"]/div[4]/div/div/div[1]/div/div/input')
    cursor.click()
    cursor = d.find_element(By.XPATH, '//*[@id="i21"]/div[6]/div[2]/div[2]/div[1]/div/input')
    cursor.send_keys(to)
    time.sleep(2)
    cursor.send_keys(Keys.ARROW_DOWN)
    cursor.send_keys(Keys.ARROW_DOWN)
    cursor.send_keys(Keys.ENTER)
    time.sleep(2)
    cursor = d.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/'
                                      'div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input')
    cursor.click()
    time.sleep(5)
    cursor = d.find_element(By.XPATH, '//*[@id="ow79"]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[3]')
    text = cursor.text
    for i, j in enumerate(text):
        if j == '₹':
            if i > 2:
                text = text[i - 3:]
            break
    l = list(map(str, text.split('\n')))
    d = defaultdict(list)
    i = 0
    while i < (len(l) // 2):
        j = l[i + 1][1:]
        j = int(j.replace(',', ""))
        d[j].append(l[i])
        i += 2
    keys = list(d.keys())
    keys.sort()
    c = 0
    for i in keys:
        print("₹", i, "flight dates with this price")
        speek("₹" + str(i) + " flight dates with this price")
        for j in d[i]:
            if c == 5:
                break
            speek(j)
            print(j, end=" ")
            c += 1
        if c == 5:
            break
    time.sleep(400)

def youtube(query):
    d = wedb()
    query = query.replace(" ","+")
    link = "https://www.youtube.com/results?search_query=+"+query
    d.get(link)
    curses = d.find_element(By.XPATH,'//*[@id="thumbnail"]/yt-image/img')
    curses.click()


a = checkin()

if a:
    print(type(a))
    cu = 3
    while True:
        l = recive(0)
        cu -= 1
        if cu==0:
            break
        print(l)
        s = list(map(str, l.split())) if l else []
        #if you say stop or cancel
        if "stop" in s or "cancel" in s:
            speek("see you next time")
            break

        #say "search flight from a to b" or just "flight a to b"
        if "flight" in s:
            l = list(map(str, l.split()))
            f = l[-3]
            t = l[-1]
            flight(f, t)

        #say "leave" or "apply leave"
        if "leave" in s:
            leave()

        #say "send a message to number or name of the person" or just "message number"
        if "message" in s:
            l = list(map(str, l.split()))
            n = l[-1]
            speek('say the message')
            k = recive()
            msg(k,n)

        #say "play x on youtube"
        if "youtube" in s:
            l = list(map(str, l.split()))
            n = "".join(l[1:-2])
            youtube(n)


        speek("can you repeate it again")
