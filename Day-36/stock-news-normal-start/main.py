import requests
import smtplib
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "IVNSWMESM8GX3Z5F"
NEWS_API_KEY = "40cefc0f79eb4730aef7806487b5fd1a"

MY_EMAIL = "adithya.mailbot@gmail.com"
PASSWORD = "bashpyjrfaocrkdu"

account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bac53485"
client = Client(account_sid, auth_token)

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(difference)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

denom = (float(yesterday_closing_price) + float(day_before_yesterday_closing_price)) / 2

percent_diff = round((difference / float(yesterday_closing_price)) * 100)
print(percent_diff)

if percent_diff > 1:
    print("Get news")
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_articles = news_response.json()["articles"]

    first_three_articles = news_articles[:3]
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{percent_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in
        first_three_articles]
    print(formatted_articles)

    for article in formatted_articles:
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            message = client.messages.create(
                body=article,
                from_="+15167306982",
                to="+919840983499",
            )

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
