from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('email/', views.SendEmail.as_view()),
    path('sms/', views.SendSMS.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
