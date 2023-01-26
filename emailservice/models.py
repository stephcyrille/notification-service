from django.db import models
from django.utils import timezone

EMAIL_CHOICES = [
    ('SIGNUP', 'Signup'),
    ('SIGNIN', 'Signin'),
    ('PASSRESREQ', 'Password reset request'),
]


class Email(models.Model):
    sender = models.EmailField(max_length=80, blank=False)
    receiver = models.CharField(max_length=250, blank=False)
    shared_receiver = models.CharField(max_length=250, blank=True)
    subject = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    joint_file = models.FileField(upload_to='emails/join_files/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    email_type = models.CharField(max_length=20, choices=EMAIL_CHOICES, default='SIGNUP')

    def __str__(self):
        return "(%s) To %s at %s" % (self.email_type, self.receiver, self.created_date.strftime("%d-%m-%Y"))
