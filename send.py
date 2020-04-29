import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='no-reply@westacebd.com',
    to_emails='nmmashnoor@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)