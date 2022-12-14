from bs4 import BeautifulSoup
import requests
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

url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B" \
      "%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.703343724016136%2C" \
      "%22north%22%3A37.847169233586946%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B" \
      "%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22" \
      "%3Atrue%7D "

response = requests.get(url=url, headers={"Accept-Language": "en-US,en;q=0.5", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"})
zillow_page = response.text

# print(zillow_page)

soup = BeautifulSoup(zillow_page, "html.parser")
# print(soup.title)

all_link_elements = soup.select(".property-card-data a")
all_link = []

for link in all_link_elements:
    href = link["href"]
    # print(href)
    if "http" not in href:
        all_link.append(f"https://www.zillow.com{href}")
    else:
        all_link.append(href)


all_address_elements = soup.select(".property-card-data address")

all_address = [address.get_text().split(" | ")[-1] for address in all_address_elements]
# print(all_address)

all_price_elements = soup.select(".hRqIYX span")
print(all_price_elements)

all_prices = [prices.get_text().split("+")[0] for prices in all_price_elements]
print(all_prices)

# Selenium

for i in range(len(all_link)):

    # Selenium
    driver = webdriver.Edge(executable_path=edge_driver, options=chr_options)

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeCyWhcGo1gi6LzyVT6OOt0ZGqzDztUxJ5Tr8WXFbD9xvTVNQ/viewform?usp=sf_link")
    time.sleep(2)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(all_address[i])

    price_per_month = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_per_month.send_keys(all_prices[i])

    link_to_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_to_property.send_keys(all_link[i])

    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_btn.click()