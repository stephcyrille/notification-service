from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_email_notification, send_sms_notification


class SendEmail(APIView):
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
