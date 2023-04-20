from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from content_app.models import News, Post, Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from seo.models import SeoPage


class SearchView(View):
    template_view = 'site_app/search.html'

    def get(self, request):
        filter_dict = {
            "title__icontains": request.GET.get("search", "")
        }
        instances = Post.objects.filter(**filter_dict)
        paginator = Paginator(instances, 12)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        get_params = dict()
        for k, v in request.GET.items():
            get_params[k] = v
        get_params.pop("page", None)
        instances = page_obj.object_list

        seo = SeoPage.objects.filter(page="search").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "page_obj": page_obj,
            "get_params": get_params,
            "posts": instances
        })


class MyProfileView(View):
    template_view = 'site_app/my-profile.html'

    def get(self, request):
        seo = SeoPage.objects.filter(page="my-profile").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "title": f"RadioCircuit | Profile",
        })
    
    def post(self, request):
        request.user.avatar = request.FILES['avatar']
        request.user.save()
        return redirect(reverse("my-profile"))


class NewsView(View):
    template_view = 'site_app/news.html'

    def get(self, request):
        instances = News.objects.all().order_by('-created')
        paginator = Paginator(instances, 12)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        get_params = dict()
        for k, v in request.GET.items():
            get_params[k] = v
        get_params.pop("page", None)
        instances = page_obj.object_list
        seo = SeoPage.objects.filter(page="news").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "page_obj": page_obj,
            "get_params": get_params,
            "news": instances
        })


class SingleNewsView(View):
    template_view = 'site_app/single-news.html'

    def get(self, request, slug):
        instance = get_object_or_404(News, slug=slug)
        instance.views += 1
        instance.save()
        return render(request, self.template_view, context={
            "seo": instance,
            "instance": instance
        })


class PostsView(View):
    template_view = 'site_app/posts.html'

    def get(self, request):
        instances = Post.objects.all()
        if "category" in request.GET:
            categories = Category.objects.filter(slug__in=[request.GET['category']])
            instances = Post.objects.filter(categories__in=[cat for cat in categories])
        instances = instances.order_by('-created')
        paginator = Paginator(instances, 12)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        get_params = dict()
        for k, v in request.GET.items():
            get_params[k] = v
        get_params.pop("page", None)
        instances = page_obj.object_list

        categories = Category.objects.all().order_by('title')
        seo = SeoPage.objects.filter(page="posts").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "posts": instances,
            "page_obj": page_obj,
            "get_params": get_params,
            "categories": categories
        })


class PostView(View):
    template_view = 'site_app/post.html'

    def get(self, request, slug):
        instance = get_object_or_404(Post, slug=slug)
        instance.views += 1
        instance.save()
        return render(request, self.template_view, context={
            "seo": instance,
            "instance": instance
        })


class HomeView(View):
    template_view = 'site_app/home.html'

    def get(self, request):
        new_posts = Post.objects.all().order_by('-created')[:6]
        popular_posts = Post.objects.all().order_by('-views')[:6]
        news = News.objects.all().order_by('-created')[:6]
        categories = Category.objects.all().order_by('title')
        seo = SeoPage.objects.filter(page="home").first() or None
        return render(request, self.template_view, context={
            "seo": seo,
            "new_posts": new_posts,
            "popular_posts": popular_posts,
            "news": news,
            "categories": categories
        })

