from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from content_app.models import News, Post

# Create your views here.


class HomeView(View):
    template_view = 'site_app/home.html'

    def get(self, request):
        new_posts = Post.objects.all().order_by('-created')[:6]
        popular_posts = Post.objects.all().order_by('-views')[:6]
        news = News.objects.all().order_by('-created')[:6]
        return render(request, self.template_view, context={
            "title": "RadioCircuit | Home",
            "new_posts": new_posts,
            "popular_posts": popular_posts,
            "news": news,
        })

