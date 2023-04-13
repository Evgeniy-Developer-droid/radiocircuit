from django import forms
from django.contrib.auth.forms import UserCreationForm
from site_app.models import User
from django.core.validators import validate_slug
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from site_app.validators import email_validation, user_email_exist_validation


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(required=True, validators=[user_email_exist_validation])

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(required=True, label='New password', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Repeat new password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    def clean_password1(self):
        password = self.cleaned_data['password1']
        self.password_cleaned = password
        validate_password(password)
        return password

    def clean_password2(self):
        cd = self.cleaned_data
        if self.password_cleaned != cd['password2']:
            raise ValidationError('Passwords don\'t match.')
        return cd['password2']


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, validators=[email_validation])

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
	
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
	    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
