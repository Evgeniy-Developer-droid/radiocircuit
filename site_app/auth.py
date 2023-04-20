from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.views import View
from seo.models import SeoPage
from site_app.models import Token, User
from site_app.forms import NewUserForm, LoginForm, ChangePasswordForm, ResetPasswordForm
from site_app.mails import recovery_password_success_mail, signup_confirm_mail, recovery_password_mail, signup_success_mail
from site_app.utils import generate_token
from django.shortcuts import get_object_or_404


class ResetPasswordView(View):
    template_view = 'site_app/reset_password.html'

    def get(self, request):
        form = ResetPasswordForm()
        seo = SeoPage.objects.filter(page="reset-password").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "form": form
        })

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        seo = SeoPage.objects.filter(page="reset-password").first() or None
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            recovery_password_mail(user.email, generate_token(user, "reset_password"))
            return render(request, self.template_view, context={
                "seo": seo,
                "form": form,
                "info": "We have sent you an email with additional instructions for changing your password."
            })
        return render(request, self.template_view, context={
            "seo": seo,
            "form": form
        })


class ChangePasswordView(View):
    template_view = 'site_app/change_password.html'

    def get(self, request, token):
        instance = get_object_or_404(Token, token=token)
        form = ChangePasswordForm()
        seo = SeoPage.objects.filter(page="change-password").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "form": form
        })

    def post(self, request, token):
        instance = get_object_or_404(Token, token=token)
        form = ChangePasswordForm(request.POST)
        seo = SeoPage.objects.filter(page="change-password").first() or None
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            instance.user.set_password(password)
            instance.user.save()
            recovery_password_success_mail(instance.user.email)
            instance.delete()
            return render(request, self.template_view, context={
                "seo": seo,
                "form": form,
                "info": "Password has been changed."
            })
        return render(request, self.template_view, context={
            "seo": seo,
            "form": form
        })


class SignupView(View):
    template_view = 'site_app/signup.html'

    def get(self, request):
        form = NewUserForm()
        seo = SeoPage.objects.filter(page="signup").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "form": form
        })

    def post(self, request):
        form = NewUserForm(request.POST)
        seo = SeoPage.objects.filter(page="signup").first() or None
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            signup_confirm_mail(user.email, generate_token(user, "signup"))
            return render(request, "site_app/signup_success.html", context={
                        "seo": seo,
                        "form": form
                    })
        return render(request, self.template_view, context={
            "seo": seo,
            "form": form
        })


class LoginView(View):
    template_view = 'site_app/login.html'

    def get(self, request):
        form = LoginForm()
        seo = SeoPage.objects.filter(page="login").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "form": form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        seo = SeoPage.objects.filter(page="login").first() or None
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            
        return render(request, self.template_view, context={
            "seo": seo,
            "form": form,
            "error": "Invalid username or password."
        })


def signup_confirm_view(request, token):
    instance = get_object_or_404(Token, token=token)
    instance.user.is_active = True
    instance.user.save()
    signup_success_mail(instance.user.email)
    instance.delete()
    seo = SeoPage.objects.filter(page="signup_confirm").first() or None
    return render(request, 'site_app/signup_confirmed.html', context={
        "seo": seo
    })
    

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))