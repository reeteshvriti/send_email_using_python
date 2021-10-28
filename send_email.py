import smtplib 
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'rititemp2@gmail.com'
email['to'] = 'reeteshvenki@gmail.com'
email['subject'] = 'Job alert'

email.set_content("Reetesh V, web developer refer this offer letter")
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('rititemp2@gmail.com', 'Riti@9741')
    smtp.send_message(email)
    print("Email sent successfully")


