
#imports
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

#end of imports

# Getting facebook username and password
facebook_username = config.facebook_username
facebook_password = config.facebook_password


edge_driver = "C:\edge1\msedgedriver"
chr_options = Options()
chr_options.add_experimental_option("detach", True)



driver = webdriver.Edge(executable_path=edge_driver, options=chr_options)

wait = WebDriverWait(driver, 20)

# Accessing tinder
driver.get("https://tinder.com/")


time.sleep(10)
# Clicking on allow cookies

allow_cookies = driver.find_element(By.XPATH, '//*[@id="s-1602360476"]/div/div[2]/div/div/div[1]/div[1]/button')
allow_cookies.click()
time.sleep(15)

# Clicking on login using XPATH
log_in_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]')
log_in_btn.click()
time.sleep(5)


# Clicking on Sign in

sign_in_btn = driver.find_element(By.XPATH, '//*[@id="s964225744"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
sign_in_btn.click()
time.sleep(5)

# # Clicking on Sign in
# more_options = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/button')
# more_options.click()

# Getting handles
# handles = driver.window_handles
# print(handles)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# Switching to fb window
driver.switch_to.window(fb_login_window)
print(driver.title)

# Entering login details

email_address_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_address_input.send_keys(facebook_username)
time.sleep(5)

password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_input.send_keys(facebook_password)
time.sleep(5)

password_input.send_keys(Keys.ENTER)
time.sleep(5)

# Switching back to Tinder Window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(10)

# Clicking on Allow location access

allow_location_access_btn = driver.find_element(By.XPATH, '//*[@id="s964225744"]/main/div/div/div/div[3]/button[1]/div[2]')
allow_location_access_btn.click()

# Clicking on Not Interested for messages:

not_interested_messages_btn = driver.find_element(By.XPATH, '//*[@id="s964225744"]/main/div/div/div/div[3]/button[2]/div[2]')
not_interested_messages_btn.click()
time.sleep(15)


#enable dark mode
dark_mode_toggle = driver.find_element(By.XPATH, '//*[@id="darkModeSwitch"]')
dark_mode_toggle.click()
time.sleep(5)

#close dark toggle

close_dark_toggle = driver.find_element(By.XPATH, '//*[@id="s964225744"]/main/div/div[2]/button')
close_dark_toggle.click()
time.sleep(5)

for n in range(100):

    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_LEFT)
    actions.perform()


driver.quit()






