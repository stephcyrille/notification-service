from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from .tasks import send_email_notification, save_email
from .serializers import SignupSerializer


class SignupEmail(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.data["first_name"]
            last_name = serializer.data["last_name"]
            receiver = serializer.data["receiver"]
            confirmation_url = serializer.data["confirmation_url"]
            subject = 'Bienvenue %s %s!' % (last_name, first_name)
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'confirmation_url': confirmation_url,
                "email_type": "SIGNUP",
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
                "email_type": "SIGNUP",
            }
            save_email.delay(email_data)
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)