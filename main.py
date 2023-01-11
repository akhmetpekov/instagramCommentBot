from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random
post = 'https://www.instagram.com/p/CnOrU_0yA7-/'
comment = '@727bro @ars.yes @teenrais'
browser = webdriver.Chrome('..chromedriver/chromedriver')

def login(username, password):

    browser.get('https://www.instagram.com')
    time.sleep(random.randrange(8, 10))

    username_input = browser.find_element(By.NAME, 'username')
    username_input.clear()
    username_input.send_keys(username)

    time.sleep(2)

    password_input = browser.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(password)

    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    browser.get(post)
    time.sleep(10)
    while True:
        for i in range(0, 9):
            cycle()
            time.sleep(3)
        time.sleep(180)

    time.sleep(10)

    browser.close()
    browser.quit()

def cycle():
    comment_input = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
    comment_input.click()
    comment_input = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
    comment_input.send_keys(comment)
    comment_input.send_keys(Keys.ENTER)

login(username, password)