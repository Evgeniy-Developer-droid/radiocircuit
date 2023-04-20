from django.urls import path
from seo import views

urlpatterns = [
    path('init-sitemap-file', views.init_sitemap_file, name="init-sitemap"),
]
