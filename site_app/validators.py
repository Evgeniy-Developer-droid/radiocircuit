from site_app.models import User
from django.core.exceptions import ValidationError


def user_email_exist_validation(email):
    instance = User.objects.filter(email=email)
    if not instance.exists():
        raise ValidationError("A user with that email not exists.")


def email_validation(email):
    instance = User.objects.filter(email=email)
    if instance.exists():
        raise ValidationError("A user with that email already exists.")