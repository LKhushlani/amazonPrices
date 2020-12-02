import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://www.amazon.in/' \
      'Kisses-Hersheys-Hersheys-Assorted-Cookies-100-8gm/dp/B0834SLRHM/ref=sr_1_1?dchild=1&keywords=kisses&qid=1606660251&s=grocery&sr=1-1'


headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text().strip()
    price = soup.find(id = 'priceblock_ourprice').get_text().strip()
    price = float(price[2:-3])

    if price < 420:
        print("Yes")
        send_email()

def send_email():
    '''
    port: 587
    When an email client or outgoing server is
    submitting an email to be routed by a proper mail server,
    it should always use SMTP port 587 as the default port.This port, coupled with TLS encryption,
    will ensure that email is submitted securely and following the guidelines set out by the IETF.

    EHLO:
    Identify yourself to an ESMTP server using EHLO

    starttls
    Put the SMTP connection in TLS (Transport Layer Security) mode.
    All SMTP commands that follow will be encrypted. You should then call ehlo() again.
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('lavinakhushlani@gmail.com', 'your pwd from 2step authentication')

    subject = 'Price dropped!'
    body = 'price dropped check the link ' + URL

    msg = f'Subject: {subject} \n\n {body}'

    # from add, to add , message
    server.sendmail('lavinakhushlani@gmail.com', 'lavinakhushlani@gmail.com', msg)

    print("Email Sent")

    server.quit()


while 1:
    check_price()
    time.sleep(24*3600)





