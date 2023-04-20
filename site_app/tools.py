from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import NoReverseMatch, reverse

from site_app.mails import signup_confirm_mail


def test_email_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        signup_confirm_mail()
        return redirect(reverse('home'))
    return HttpResponse("You haven`t permissions!")