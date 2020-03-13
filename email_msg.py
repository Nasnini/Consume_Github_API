import os;
import smtplib;

#Change depending on what is the 3rd party variable
EMAIL_ADDRESS = os.environ.get('Email_Users') 
EMAIL_PASSWORD = os.environ.get('Email_Pass') 

with smtplib.SMTP('smtp.gmail.com', 587) as SMTP:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'This is the subject line of the inspirational email'
    body = 'This is the funny bit where you gag and roll on the floor laughing at whatever shit is beiong said'

    msg = f'Subject: {subject} \n\n\n {body}'

smtp.sendmail(EMAIL_ADDRESS, 'newkobuoe@gmail.com' msg)