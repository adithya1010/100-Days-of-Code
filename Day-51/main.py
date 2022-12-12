# imports
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions as excp
from selenium.webdriver.common.action_chains import ActionChains
import time
from time import sleep

import config

edge_driver = "C:\edge1\msedgedriver"
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# end of imports

# Speeds in MBPS promised by Jio according to plan

PROMISED_DOWN = 30
PROMISED_UP = 30

# Getting twitter username and password from config.py
twitter_username = config.twitter_email
twitter_password = config.twitter_password


# driver = webdriver.Edge(executable_path=edge_driver, options=chr_options)
# driver.get("https://www.speedtest.net/")

class InternetSpeedBot:
    def __init__(self, driver_path, browser_options):
        self.driver = webdriver.Edge(executable_path=driver_path, options=browser_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_btn = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"down: {self.down}")
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH,
                                               '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(twitter_username)
        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(4)
        username_input = self.driver.find_element(By.NAME, 'text')
        username_input.send_keys("SpeedBotAdithya")
        username_input.send_keys(Keys.ENTER)
        time.sleep(4)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(twitter_password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(7)
        tweet_text = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        message = f"Hey @reliancejio my internet speed is: Download:{self.down} Mbps, Upload:{self.up} Mbps"
        tweet_text.send_keys(message)
        # tweet_text.send_keys(Keys.ENTER)
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()


speed_bot = InternetSpeedBot(edge_driver, chr_options)
speed_bot.get_internet_speed()
speed_bot.tweet_at_provider()
