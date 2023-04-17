from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.templatetags.static import static


def signup_confirm_mail(email, token):
    try:
        link = f"{settings.SITE_URL}{reverse('signup_confirm', args=(token,))}"
        logo = f"{settings.SITE_URL}{static('logo.svg')}"

        subject = 'Sign up confirm'
        html_message = render_to_string('mails/signup_confirm.html', {'link': link, "logo": logo})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = [email]

        send_mail(subject, plain_message, from_email, to, html_message=html_message)

    except Exception as e:
        print(e)


def signup_success_mail(email):
    try:
        logo = f"{settings.SITE_URL}{static('logo.svg')}"

        subject = 'Sign up confirm'
        html_message = render_to_string('mails/signup_success.html', {"logo": logo})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = [email]

        send_mail(subject, plain_message, from_email, to, html_message=html_message)

    except Exception as e:
        print(e)


def recovery_password_mail(email, token):
    try:
        link = f"{settings.SITE_URL}{reverse('change-password', args=(token,))}"
        logo = f"{settings.SITE_URL}{static('logo.svg')}"

        subject = 'Change password'
        html_message = render_to_string('mails/change_password.html', {'link': link, "logo": logo})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = [email]

        send_mail(subject, plain_message, from_email, to, html_message=html_message)

    except Exception as e:
        print(e)


def recovery_password_success_mail(email):
    try:
        logo = f"{settings.SITE_URL}{static('logo.svg')}"

        subject = 'Change password success'
        html_message = render_to_string('mails/change_password_success.html', {"logo": logo})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = [email]

        send_mail(subject, plain_message, from_email, to, html_message=html_message)

    except Exception as e:
        print(e)
