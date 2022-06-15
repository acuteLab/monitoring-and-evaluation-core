from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Union, Optional, List
import smtplib

from jinja2 import Template

from settings import TESTING
from settings import SMTP_HOST
from settings import SMTP_PORT
from settings import SMTP_USERNAME
from settings import SMTP_PASSWORD


def send_email(to_email: str, subject: str, body: str):
    """Send an email."""
    msg = MIMEMultipart("alternative")
    # me == the sender's email address
    # you == the recipient's email address
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME
    msg["To"] = to_email

    # Get the contents of the template.
    with open("config/notifications/email_template/email.html", "r") as template:
        # Parse
        template = Template(template.read())
    # inject the body.
    text = body
    html = template.render(body=body)

    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    if TESTING:
        # Do not send an actual email if unittesting.
        return
    smtpObj = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    smtpObj.starttls()
    smtpObj.login(SMTP_USERNAME, SMTP_PASSWORD)
    smtpObj.send_message(msg)
    smtpObj.quit()
