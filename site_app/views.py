from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

# Create your views here.


class HomeView(View):
    template_view = 'site_app/home.html'

    def get(self, request):
        return render(request, self.template_view, context={
            "title": "RadioCircuit | Home"
        })

