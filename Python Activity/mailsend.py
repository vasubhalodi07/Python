import smtplib
from matplotlib import scale
import config
import pyqrcode
import png
from pyqrcode import QRCode

email = input("Enter Your Email Id: ")

def send_email (subject, msg):
    try:
        if pyqrcode.create(email):
            png('myqr.png', scale=6)
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            message = "subject {} \n\n {}".format(subject, msg)
            server.sendmail(config.EMAIL_ADDRESS, email, message)
            server.quit()
            print("Email Successfully Send")
    except:
        print("Email failed to send")

subject = "Mail Send Using Python"
msg = "for knowlonge"

send_email(subject, msg)
