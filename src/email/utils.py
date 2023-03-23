from src.email import email_sender

def send_email(recipients, content, subject):
    email_sender.send_email(recipients, content, subject)