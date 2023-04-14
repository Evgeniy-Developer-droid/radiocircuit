from django.urls import path
from site_app import views
from site_app import auth

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('posts', views.PostsView.as_view(), name="posts"),
    path('post/<slug:slug>', views.PostView.as_view(), name="post"),

    # auth
    path('login', auth.LoginView.as_view(), name="login"),
    path('sign-up', auth.SignupView.as_view(), name="signup"),
    path('logout', auth.logout_view, name="logout"),
    path('sign-up/confirm/<str:token>', auth.signup_confirm_view, name="signup_confirm"),
    path('reset-password', auth.ResetPasswordView.as_view(), name="reset-password"),
    path('change-password/<str:token>', auth.ChangePasswordView.as_view(), name="change-password"),
]
