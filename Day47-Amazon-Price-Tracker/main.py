from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv('my_email')
PASSWORD = os.getenv('password')
TARGET_PRICE = 22.00
ITEM_LINK = "https://www.amazon.com/Genuine-Instant-Pot-Tempered-lid/dp/B01K7XKN8I/ref=ex_alt_wg_d?_encoding=UTF8&pf_rd_r=QKWF7FH3CV3587E9SN6X&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pd_rd_i=B01K7XKN8I&pd_rd_w=TX3Bj&pd_rd_wg=84XHg&pd_rd_r=4b319c56-cdd1-4bd4-9e5b-b7377ea95518&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699&th=1"

response = requests.get(
    url = ITEM_LINK,
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8,fa;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    },
)

soup = BeautifulSoup(response.text, "html.parser")
whole_tag = soup.find(name='span', class_='a-offscreen').getText().replace("$", "")
current_price = float(whole_tag)

title_tag = soup.find(name='span', id="productTitle")
title_text = title_tag.getText()
title_list = title_text.split()
title = ''
for word in title_list:
    title += word + " "

#print(title)

with smtplib.SMTP("smtp.gmail.com", 587) as con:
    con.starttls()
    con.login(user=MY_EMAIL, password=PASSWORD)
    if current_price < TARGET_PRICE:
        con.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ultra_boy_360@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{title} is on sale for {current_price}.\n{ITEM_LINK}".encode("utf-8")
        )


