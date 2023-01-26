from django.core import mail
from celery import shared_task
from decouple import config
from .models import Email


@shared_task
def send_email_notification(subject, html_message, plain_text_message, recipient_list):
    # Code pour envoyer un email ici
    mail.send_mail(subject, plain_text_message, recipient_list=recipient_list, html_message=html_message,
                   from_email="YOK Exchange <%s>" % (config("DEFAULT_FROM_EMAIL", default='info@localhost')))
    return "Email sent!"


@shared_task
def save_email(data):
    Email.objects.create(**data)
    return "email saved"


@shared_task
def send_sms_notification(phone_number, message):
    # Code pour envoyer un SMS ici
    print('Envoi d\'un SMS à {} avec le message : {}'.format(phone_number, message))
