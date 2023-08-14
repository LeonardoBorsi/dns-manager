from django.urls import path
from .views import (HomePageView, RegisterPageView, LoginPageView, LogoutPageView, ProfilePageView, CreateSuperuserView)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('register', RegisterPageView.as_view(), name='register'),
    path('login', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('profile', ProfilePageView.as_view(), name='profile'),
    #path('create-superuser', CreateSuperuserView.as_view(), name='create-superuser'),
]