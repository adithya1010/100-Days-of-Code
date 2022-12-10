
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
import time
import config
#end of imports

linkedin_username = config.linkedin_username
linkedin_password = config.linkedin_password

edge_driver = "C:\edge1\msedgedriver"
chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Edge(executable_path=edge_driver, options=chr_options)
time.sleep(2)

# Credentials



wait = WebDriverWait(driver, 20)
# Opening linkedin in edge
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3371304260&f_LF=f_AL&geoId=114467055&keywords=python%20developer&location=Chennai%2C%20Tamil%20Nadu%2C%20India&refresh=true")

# Clicking on Sign in button
sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_btn.click()

# Interacting with Search

username = driver.find_element(By.ID, "username")
username.send_keys(linkedin_username)
password = driver.find_element(By.ID, "password")
password.send_keys(linkedin_password)

password.send_keys(Keys.ENTER)


#Locate the apply button
# apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
# apply_button.click()

# Clicking on save button


all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")


for listing in all_listings:
    listing.click()
    time.sleep(2)
    apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
    apply_button.click()
    time.sleep(5)
    try:

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.text == "Next":
            close_button = driver.find_element(By.CSS_SELECTOR, "#artdeco-modal-outlet button")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex Application, Skipped")
            continue
        else:
            submit_button.click()
            print("Application Submitted")
        # After application Submitted LinkedIn will show a pop-up to take assesment.
        time.sleep(2)
        take_assesment_close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal-outlet")
        take_assesment_close_button.click()
    except NoSuchElementException:
            print("No application button, Skipped.")
            continue

# time.sleep(5)
# driver.quit()








