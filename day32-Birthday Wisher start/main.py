# import smtplib
#
# my_email="texperiment660@gmail.com"
# password="g3tScr3w3dm8#d3Ad"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="experi121te89@yahoo.com",
#                         msg="Subject:Hello\n\n This is the body of my email")

# import smtplib
#
# my_email="experi121te89@yahoo.com"
# password="NuM8@$$Nu88!e"
# #Noted that there is a port number (587) being put into the connection due to TIMEOUT error
# with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="texperiment660@gmail.com",
#                         msg="Subject:Hello\n\n This is the body of my email")

import datetime as dt
import random
import smtplib

now=dt.datetime.now()
year=now.year
month=now.month
day=now.weekday()

print(day)
with open("quotes.txt") as quote:
    lines=quote.readlines()

random_message=random.choice(lines)
my_email="texperiment660@gmail.com"
password="g3tScr3w3dm8#d3Ad"

if day==4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="experi121te89@yahoo.com", msg=f"Subject: Hello!\n\n{random_message}")