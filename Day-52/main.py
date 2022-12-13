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


SIMILAR_ACCOUNT = "jk16377"

INSTA_USERNAME = config.USERNAME
INSTA_PASSWORD = config.PASSWORD


class InstaFollower:
    def __init__(self, driver_path, browser_options):
        self.driver = webdriver.Edge(executable_path=driver_path, options=browser_options)
        self.down = 0
        self.up = 0

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username_input = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        username_input.send_keys(INSTA_USERNAME)
        password_input = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        password_input.send_keys(INSTA_PASSWORD)
        time.sleep(2)
        login_btn = self.driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
        login_btn.click()
        time.sleep(5)
        not_now_btn = self.driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        not_now_btn.click()
        time.sleep(2)
        not_now_notifications_btn = self.driver.find_element(By.XPATH,
                                                             '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_now_notifications_btn.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(2)


    def follow(self):
        # followers
        time.sleep(2)
        modal = self.driver.find_element(By.CSS_SELECTOR, '._ab8w ._aano')
        try:
            list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            for item in list_of_followers:
                time.sleep(3)
                print(item.text)
                if item.text == "Follow":
                    print("click")
                    item.click()

        except Exception as e:
            print(e)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

        # scr1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]')


insta_bot = InstaFollower(edge_driver, chr_options)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
