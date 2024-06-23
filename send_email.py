import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# e-mail information
sender_email = "sender_email@example.com"
receiver_email = "receiver_email@example.com"
password = "sender_password"
subject = "Test Mail"
body = "This is a test email sent from Python."

# e-mail content
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # SMTP shell
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()  # start a secure shell
    server.login(sender_email, password)  # login
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)  # send an e-mail
    server.quit()  # quit collection
    print("The email was sent successfully.")
except smtplib.SMTPAuthenticationError:
    print("Kimlik doğrulama hatası: Kullanıcı adı veya şifre yanlış.")
except Exception as e:
    print(f"Email sending error: {e}")
