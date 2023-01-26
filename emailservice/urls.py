from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .signup import SignupEmail
from .signin import SigninEmail
from .password_reset import PasswordResetRequestEmail

urlpatterns = [
    path('email/signup/', SignupEmail.as_view()),
    path('email/signin/', SigninEmail.as_view()),
    path('email/password-reset/request/', PasswordResetRequestEmail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
