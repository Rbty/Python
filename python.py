from asyncio import sleep
from selenium import webdriver
import time

nick = input('Insert your nickname:')
password = input('Insert your password:')

browser = webdriver.Firefox()
browser.get(url='https://www.roblox.com/login')


USERNAME = nick
PASSWORD = password


browser.find_element('xpath','//*[@id="login-username"]').send_keys(USERNAME)
time.sleep(0.1)
browser.find_element('xpath','//*[@id="login-password"]').send_keys(PASSWORD)
time.sleep(0.1)
browser.find_element('xpath','//*[@id="login-button"]').click()
time.sleep(2)
browser.find_element('xpath','/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/button[2]').click()
time.sleep(2)
browser.find_element('xpath','//*[@id="nav-character"]').click()
time.sleep(2)
browser.find_element('xpath','/html/body/div[3]/div[2]/div[2]/div[3]/div/div/div[7]/div[2]/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/div[1]/a').click()











