import smtplib

from django.core.mail import send_mail
from django.template.loader import render_to_string

from LPGallery import settings
from LPGallery.celery import app


@app.task
def send_users_amount():
    server = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
    server.starttls()
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    send_mail(
        subject='This email was sent via celery',
        message='Hello!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[],
        html_message=render_to_string('security/schedule_task.html', {})
    )