# import smtplib as smtp
#
# my_email = "adist1340@gmail.com"
# password = "nlekwkjctodavyfb"
#
# with smtp.SMTP_SSL('smtp.gmail.com', 465) as connection:  # SSL is a protocol to secure the connection
#     connection.login(user=my_email, password=password)  # Logging in using username and password
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="vani1340@gmail.com",
#         msg="Subject:Test message\n\nBody of email"
#     )  # sending mail with from
# # address, to address and message

# Using datetime module to get the current time
# import datetime as dt
#
# now = dt.datetime.now()  # now function returns current time and date
# # Getting year, month and day of the week from now
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# # Creating a custom date and time object
# date_of_birth = dt.datetime(year=2000, month=10, day=10)
# print(date_of_birth)

# Monday Motivational quote project:
import smtplib as smtp
import datetime as dt
MY_EMAIL = "adithya.mailbot@gmail.com"
PASSWORD = "bashpyjrfaocrkdu"
import random
now = dt.datetime.now()  # now function returns current time and date
# Getting year, month and day of the week from now
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 0:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        today_quote = random.choice(quotes)
    with smtp.SMTP_SSL('smtp.gmail.com', 465) as connection:  # SSL is a protocol to secure the connection
        connection.login(user=MY_EMAIL, password=PASSWORD)  # Logging in using username and password
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="adist1340@gmail.com",
            msg=f"Subject:Monday Motivation Quote\n\n{today_quote}"
        )  # sending mail with from
    # address, to address and message

