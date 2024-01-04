import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url="https://www.amazon.in/BenQ-23-8-inch-Monitor-Built/dp/B073NTCT4Q/ref=sr_1_5?dchild=1&keywords=monitor&qid=1631012056&sr=8-5&th=1"
headers={
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Defined"
}

response=requests.get(url=url, headers=headers)
amazon_details=response.text
soup=BeautifulSoup(amazon_details, "lxml")
whole_price=soup.select(".a-price-whole")[0].getText()[:-1]

new_price=int(("").join(whole_price.split(','))) if ',' in whole_price else int(whole_price)

print(new_price)

title=soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE=14000
my_email="texperiment660@gmail.com"
password="g3tScr3w3dm8#d3Ad"

if new_price<BUY_PRICE:
    message=f"{title} is now at price of {new_price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="experi121te89@yahoo.com",
                            msg=f"Subject:CHEAP PRICE NOW @ AMAZON!\n\n{message}")