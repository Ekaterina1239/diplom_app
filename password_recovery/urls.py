from django.urls import path, include

from password_recovery.accounts.views import password_reset

urlpatterns = [
    # ...
    path('password-reset/', password_reset, name='password_reset'),
]