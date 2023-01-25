# Generated by Django 3.2 on 2023-01-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='email_type',
            field=models.CharField(choices=[('SIGNUP', 'Signup'), ('SIGNIN', 'Signin')], default='SIGNUP', max_length=20),
        ),
    ]
