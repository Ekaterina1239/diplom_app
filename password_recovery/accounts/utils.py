from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def send_password_reset_email(user):
    current_site = get_current_site(request=None)
    mail_subject = 'Password Reset'
    message = render_to_string(
        'accounts/reset_password_email.html',
        {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        }
    )
    send_mail(mail_subject, message, 'sender@example.com', [user.email])