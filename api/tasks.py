from celery import shared_task


@shared_task
def send_email_notification(email, message):
    # Code pour envoyer un email ici
    print('Envoi d\'un email à {} avec le message : {}'.format(email, message))


@shared_task
def send_sms_notification(phone_number, message):
    # Code pour envoyer un SMS ici
    print('Envoi d\'un SMS à {} avec le message : {}'.format(phone_number, message))
