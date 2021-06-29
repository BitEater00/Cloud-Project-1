from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY= #key

def subscription_email(id):
    to = id.decode('utf-8')
    email_body = Mail(
    from_email=#from email,
    to_emails = to,
    subject= 'Subscription Email from VIT-AP club tech team',
    html_content='<h2>Thank you </h2><br><h3>Your Subscription to club has been confirmed</h3>')
    send_email(email_body)

def registration_email(id):
    to = id.decode('utf-8')
    email_body = Mail(
    from_email=#from email,
    to_emails = to,
    subject= 'Subscription Email from VIT-AP club tech team',
    html_content='<h2>Thank you </h2><br><h3>Your registration for the event  has been confirmed</h3>')
    send_email(email_body)

def send_email(message):
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        print(e.message)