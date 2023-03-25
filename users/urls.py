from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path("",views.home,name="home"),

    path("register/", views.register,name="register"),
    path("profile/",views.profile,name="profile"),
    path("results/", views.results,name="results"),

    path("login/",auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout")

]
