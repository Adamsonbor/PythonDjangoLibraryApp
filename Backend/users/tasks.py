from django.core.mail import send_mail
from celery import shared_task
from settings.settings import EMAIL_HOST_USER

@shared_task
def send_email(to_email, username):
    # Email subject
    subject = 'Hello from celery'

    # Email body with HTML tags
    message = (
        f'Hi 👋 {username},<br>'
        'Welcome to the best site written in Django<br>'
        'Thanks for joining us. We hope you enjoy your stay<br>'
        '<br><br>'
        f'From: {EMAIL_HOST_USER}<br>'
        f'To: {to_email}'
    )

    # Sending email using Django's send_mail function
    send_mail(subject,
              "",
              EMAIL_HOST_USER,
              [to_email],
              fail_silently=False, 
              html_message=message)
