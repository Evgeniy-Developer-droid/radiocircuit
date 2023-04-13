from django.core.mail import send_mail
from django.urls import reverse


def signup_confirm_mail(email, token):
    send_mail(
        'sign up confirm',
        f"{reverse('signup_confirm', args=(token,))}",
        'admin@gmail.com',
        [email],
        fail_silently=False,
    )


def signup_success_mail(email):
    send_mail(
        'sign up success',
        'Here is the message.',
        'admin@gmail.com',
        [email],
        fail_silently=False,
    )


def recovery_password_mail(email, token):
    send_mail(
        'recovery password',
        f"{reverse('change-password', args=(token,))}",
        'admin@gmail.com',
        [email],
        fail_silently=False,
    )


def recovery_password_success_mail(email):
    send_mail(
        'recovery passsword success',
        'Here is the message.',
        'admin@gmail.com',
        [email],
        fail_silently=False,
    )
