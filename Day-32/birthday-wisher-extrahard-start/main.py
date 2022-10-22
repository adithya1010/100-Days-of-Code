##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.

# Using pandas to read the csv file:
import pandas
import random
import smtplib
birthday_data = pandas.read_csv("birthdays.csv")


MY_EMAIL = "adithya.mailbot@gmail.com"
PASSWORD = "bashpyjrfaocrkdu"

import datetime as dt
today = dt.datetime.now()

today_tuple = (today.month, today.day)
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_data.iterrows()}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)  # Logging in using username and password
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )  # sending mail with from
    # address, to address and message
