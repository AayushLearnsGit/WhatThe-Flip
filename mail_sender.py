import smtplib
from email.message import EmailMessage
import os, pickle



def send_email(title, prod_url, old_price, new_price):
    with open("config", "rb") as f:
        credentials = pickle.load(f)

    template=f'''\
<!DOCTYPE html>
<html>
<body>
<h2> Let's Talk Price. </h2>
<font face="consolas" size= 5> Now, </font> <br>
<font size= 7> {title} </font> is buyable! <br>
<br>
<br>
<font face="consolas" size= 5> Before,
    <font face="consolas" size= 5><br>
        <strike> ₹ {old_price} </strike>
    </font>
</font> <br>

<font face="consolas" size= 5> Now,
    <b>
        <font face="consolas" size= 7><br>
        ₹ {new_price}
        </font>
    </b>
</font> <br>

Get it on: <a href="{prod_url}">Product Link</a>
</body>
</html>
'''
    my_email = credentials["email"]
    my_pass = credentials["password"]

    message = EmailMessage()
    message['Subject'] = "Hey! Price has dropped - Check it out"
    message['From'] = my_email
    message['To'] = credentials["target"]
    message.set_content('The temprory message, read this? Now delete this.')

    message.add_alternative(template, subtype= 'html')

    print("[SENDING MESSAGE]")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(my_email, my_pass)
        smtp.send_message(message)
    print("[MESSAGE SENT]")