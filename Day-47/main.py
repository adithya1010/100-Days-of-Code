import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
MY_EMAIL = "adithya.mailbot@gmail.com"
PASSWORD = "bashpyjrfaocrkdu"
url = "https://www.amazon.in/Pikkme-Redmi-Magnetic-Leather-Shockproof/dp/B08L9HDBGQ/ref=lp_21360365031_1_1"
response = requests.get(url=url, headers={"Accept-Language": "en-US,en;q=0.5", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"})
amazon_mobile_page = response.text

soup = BeautifulSoup(amazon_mobile_page, "lxml")
price = soup.find("span", class_="a-offscreen").getText().split("₹")[1]
# print(price)
price_as_float = float(price)

print(price_as_float)
# Message

title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").text
print(title)

message = f"{title} is now {price}\n{url}"

# print(message)

base_price = 200

if price_as_float < base_price:
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)  # Logging in using username and password
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="adist1340@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )  # sending mail with from
    # address, to address and message

