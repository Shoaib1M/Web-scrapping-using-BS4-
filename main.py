import requests
from bs4 import BeautifulSoup
import smtplib

response=requests.get("**AMAZON ITEM LINK**")

data=response.text

soup=BeautifulSoup(data,"html.parser")

price = soup.find(class_="a-offscreen").get_text()
print(price[1:])

if price<("YOUR SPECIFIED AMOUNT"):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login("YOUR EMAIL", "****************")
    connection.sendmail(
        from_addr="YOUR EMAIL",
        to_addrs="YOUR EMAIL",
        msg="Alert low price!!\n\nThe product you wanted is at an all time low!! BUY NOW!!"
    )