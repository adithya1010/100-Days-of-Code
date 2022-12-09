# Setting up Selenium for Edge
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
edge_driver = "C:\edge1\msedgedriver"
chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Edge(executable_path=edge_driver, options=chr_options)

# Opening amazon in edge
driver.get("https://www.python.org/")

wait = WebDriverWait(driver, 20)

# Find element by ID
# wait.until(EC.visibility_of_element_located((By.ID, 'a-offscreen'))) # gives an implicit wait for 20 seconds
# price = driver.find_element(By.ID, "a-offscreen")
# print(price)

# find element by name:
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# # Find element by class name:
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# # Find element by css selectors:
#
# link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(link.text)
#
# # Find element by Xpath:
#
# bug_link = driver.find_element(By.XPATH, "/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

# Event times are stored in a class called event-widget and in a time tag
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_times:
#     print(time.text)

# Event names are stored in a class called event-widget and in a li and a tag
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}

# Storing the event time and names in a nested dictionary
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)





# Close site:
driver.quit()

