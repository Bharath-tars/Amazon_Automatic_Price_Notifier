import requests
import smtplib
from bs4 import BeautifulSoup
import lxml
mail_password=""
parameters= {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}
amazon_link=""
responce= requests.get(url=amazon_link, headers=parameters)
responce_text = responce.text

soup = BeautifulSoup(responce_text, "lxml")
price = soup.find(name="span", class_="a-offscreen")
with smtplib.SMTP("smtp.gmail.com") as connection:
    if price.getText() == "₹1,499.00":
        connection.starttls()
        connection.login(user="",password=mail_password)
        connection.sendmail(to_addrs="",from_addr="",msg=f"Subject : Buy the"
                                                                                                             f" fuckin airdopes \n\n\n "
                                                                                                               f"Now it is 1499 only\n\n"
                                                                                                               f"click :{link_url}",)
print("mail sent")
