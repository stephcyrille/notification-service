from django.core import mail
from celery import shared_task
from django.template.loader import render_to_string
from decouple import config

@shared_task
def send_email_notification(subject, template_html, template_txt, context, recipient_list):
    # Code pour envoyer un email ici
    html_message = render_to_string(template_html, context)
    plain_message = render_to_string(template_txt, context)
    mail.send_mail(subject, plain_message, recipient_list=recipient_list, html_message=html_message,
                   from_email=config("DEFAULT_FROM_EMAIL", default='info@localhost'))
    return "Email sent!"

    # TODO create another task for persisting email in DB

@shared_task
def send_sms_notification(phone_number, message):
    # Code pour envoyer un SMS ici
    print('Envoi d\'un SMS à {} avec le message : {}'.format(phone_number, message))
