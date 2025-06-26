import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Use 465 for SSL or 587 for TLS
USERNAME = ""  # Your email login
PASSWORD = ""  # Your email password

sender_email = ''
receiver_email = ''

subject = 'Test email from python'
body = 'This email is sent via python code'

# Create the email object
message = MIMEText(body, 'plain')  # "plain" means text-only email
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

# Create an SMTP session
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Secure the connection
    server.login(USERNAME, PASSWORD)  # Log in to SMTP server
    server.sendmail(sender_email, receiver_email, message.as_string())  # Send email