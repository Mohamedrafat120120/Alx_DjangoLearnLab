from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from .views import *
urlpatterns = [
    path('register/',register.as_view(),name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/',profile.as_view(),name="profile"),
    path('home/',home.as_view(),name="home"),
    path('posts/',posts.as_view(),name="posts"),
]