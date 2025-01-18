from django.shortcuts import render
from .utils import send_password_reset_email
# Create your views here.
def password_reset(request):
    send_password_reset_email(user)
    return HttpResponse('Password recovery email sent.')