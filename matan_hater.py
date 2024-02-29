# -*- coding: windows-1251 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option(
    'prefs', 
    {
        'profile.managed_default_content_settings.javascript': 2,
        'profile.managed_default_content_settings.images': 2,
        'profile.managed_default_content_settings.mixed_script': 2,
        'profile.managed_default_content_settings.media_stream': 2,
        'profile.managed_default_content_settings.stylesheets':2
    })
driver = webdriver.Edge(options=options)




def aut(login, password):
    driver.get("https://moodle.surgu.ru/login/index.php")
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"username").send_keys(login)
    #print("AUT: SUCCSESS")

def cont():
    driver.find_element(By.XPATH,"//button[text()='Продолжить']").click()

def ans(path):
    f=open(path,encoding="utf-8")
    start=f.readline().rstrip('\n')
    driver.get(f.readline().rstrip('\n'))
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            #print("BREAK")
            break
        
        a=line.split()
        
        if a[0]=='checkbox':
            for i in range(int(a[1])):
                driver.find_element(By.ID,f.readline().rstrip('\n')).click()
            driver.find_element(By.ID,'id_submitbutton').click()
            cont()
            
        elif a[0]=='menu':
            for i in range(int(a[1])):
                b=f.readline().split()
                Select(driver.find_element(By.ID, b[0])).select_by_value(b[1])
            driver.find_element(By.ID,'id_submitbutton').click()          
    driver.get(start)
    

try:
    t=time.time()
    f=open("login.txt")
    login=f.readline()
    password=f.readline()
    aut(login,password)
    for i in range(25):
        ans("4.2 config.txt")
    print(time.time()-t)
except:
    print("ERROR!")
