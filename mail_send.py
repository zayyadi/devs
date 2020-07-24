import smtplib
from email.mime.text import MIMEText

def mail_send(customer,marketer, product, size):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '1902ec824c2953'
    password = '7365f34d9afdd9'
    message = f"<h3>New Product Catalogue</h3><ul><li>Customer: {customer}</li> <li>marketer: {marketer}</li> <li>product: {product}</li<li>size: {size}</li></ul>"

    sender_email = 'email1@emaple.com'
    reciever_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Product Catalogue'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())