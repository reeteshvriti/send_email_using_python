import smtplib 
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'enter sender email address'
email['to'] = 'enter the email address of the reciver'
email['subject'] = 'Job alert'

email.set_content("alert for job as web developer")
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender email address', 'password of email')
    smtp.send_message(email)
    print("Email sent successfully")


