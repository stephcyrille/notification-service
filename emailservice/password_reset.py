from django.template.loader import render_to_string
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from .tasks import send_email_notification, save_email
from .serializers import PasswordResetRequestSerializer


class PasswordResetRequestEmail(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            receiver = serializer.data["receiver"]
            reset_url = serializer.data["reset_url"]
            subject = 'Requête de Réinitialisation du mot de passe'
            context = {
                "email_type": "PASSRESREQ",
                "reset_url": reset_url,
                "user_email": receiver,
                "ip_address": "192.168.258.212",
                "day_date": timezone.now(),
            }
            recipient_list = (receiver,)
            html_message = render_to_string('mail_template.html', context)
            plain_message = render_to_string('mail_template.txt', context)
            # Send email task to celery worker
            send_email_notification.delay(subject, html_message, plain_message, recipient_list)
            # Send email saving task to celery worker
            email_data = {
                "sender": config("DEFAULT_FROM_EMAIL", default='info@localhost'),
                "receiver": receiver,
                "subject": subject,
                "content": html_message,
                "email_type": "PASSRESREQ",
            }
            save_email.delay(email_data)
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)