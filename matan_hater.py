# -*- coding: windows-1251 -*-
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from progress.bar import IncrementalBar



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
    t=time.time()
    driver.get("https://moodle.surgu.ru/login/index.php")
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"username").send_keys(login)
    print(f"AUTHORIZATION COMPLITED IN {round(time.time()-t, 2)} SECONDS")

def cont():
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[text()='Продолжить']").click()

def ans(path):
    f=open(path,encoding="utf-8")
    start=f.readline().rstrip('\n')
    driver.get(f.readline().rstrip('\n'))
    b=[]
    while True:
        line = f.readline().rstrip('\n')
        if not line:
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
                Select(driver.find_element(By.ID, b[0])).select_by_value(' '.join(b[1:]))
            driver.find_element(By.ID,'id_submitbutton').click()
        elif a[0]=='input':
            driver.find_element(By.ID,'id_answer').send_keys(a[1])
            driver.find_element(By.ID,'id_submitbutton').click()
    driver.get(start)

def main(path, times):
    bar = IncrementalBar('PROGRESS', max = times)
    try:
        t=time.time()
        f=open("login.txt",encoding="utf-8")
        login=f.readline()
        password=f.readline()
        aut(login,password)
        bar.start()
        for i in range(times):
            ans(path)
            bar.next()
        bar.finish()
        print(f"{i+1} ITERATIONS COMPLITED IN {round(time.time()-t, 2)} SECONDS")
    except Exception as e:
        print("\nERROR\n")
        print(e)

main("4.5 config.txt", 196)