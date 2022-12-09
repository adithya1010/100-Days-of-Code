from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
edge_driver = "C:\edge1\msedgedriver"
chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Edge(executable_path=edge_driver, options=chr_options)

# Opening wikipedia in edge
driver.get("https://en.wikipedia.org/wiki/Main_Page")

wait = WebDriverWait(driver, 20)

# No of articles from wikipedia
# The article count is in an Id called articlecount and under an anchor tag
no_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(no_of_articles.text)

# Clicking on content portals

content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()

# Interacting with Search

search = driver.find_element(By.NAME, "search")
# Typing python in the search bara
search.send_keys("Python")
search.send_keys(Keys.ENTER)
