from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('email/signup/', views.SignupEmail.as_view()),
    path('email/send/bulk/', views.SendBulkEmail.as_view()),
    path('sms/', views.SendSMS.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
