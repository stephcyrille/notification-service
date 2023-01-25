from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_email_notification, send_sms_notification
from .serializers import SignupSerializer


class SignupEmail(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.data["first_name"]
            last_name = serializer.data["last_name"]
            receiver = serializer.data["receiver"]
            confirmation_url = serializer.data["confirmation_url"]
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'confirmation_url': confirmation_url,
            }
            recipient_list = (receiver,)
            subject = 'Bienvenue %s %s!' % (last_name, first_name)
            template_html = 'mail_template.html'
            template_txt = 'mail_template.txt'
            send_email_notification.delay(subject, template_html, template_txt, context, recipient_list)
            # TODO call another task for persisting email in DB
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninEmail(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.data["first_name"]
            last_name = serializer.data["last_name"]
            receiver = serializer.data["receiver"]
            confirmation_url = serializer.data["confirmation_url"]
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'confirmation_url': confirmation_url,
            }
            recipient_list = (receiver,)
            subject = 'Bienvenue %s %s!' % (last_name, first_name)
            template_html = 'mail_template.html'
            template_txt = 'mail_template.txt'
            send_email_notification.delay(subject, template_html, template_txt, context, recipient_list)
            # TODO call another task for persisting email in DB
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendBulkEmail(APIView):
    def post(self, request):
        email = request.data.get('email')
        message = request.data.get('message')
        send_email_notification.delay(email, message)
        return Response({'status': 'success'})


class SendSMS(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        message = request.data.get('message')
        send_sms_notification.delay(phone_number, message)
        return Response({'status': 'success'})
