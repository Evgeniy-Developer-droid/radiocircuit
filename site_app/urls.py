from django.urls import path
from site_app import views
from site_app import auth
from django.conf import settings

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('posts', views.PostsView.as_view(), name="posts"),
    path('post/<slug:slug>', views.PostView.as_view(), name="post"),
    path('news', views.NewsView.as_view(), name="news"),
    path('news/<slug:slug>', views.SingleNewsView.as_view(), name="single-news"),

    path('my-profile', views.MyProfileView.as_view(), name="my-profile"),
    path('search', views.SearchView.as_view(), name="search"),

    # auth
    path('login', auth.LoginView.as_view(), name="login"),
    path('sign-up', auth.SignupView.as_view(), name="signup"),
    path('logout', auth.logout_view, name="logout"),
    path('sign-up/confirm/<str:token>', auth.signup_confirm_view, name="signup_confirm"),
    path('reset-password', auth.ResetPasswordView.as_view(), name="reset-password"),
    path('change-password/<str:token>', auth.ChangePasswordView.as_view(), name="change-password"),
]
