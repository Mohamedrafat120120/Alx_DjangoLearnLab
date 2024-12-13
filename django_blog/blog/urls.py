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
    path('display/',display.as_view(),name="display"),
    path('post/new/',display_create.as_view(),name="display_create"),
    path('display_detail/<int:pk>/',display_detail.as_view(),name="display_detail"),
    path('post/<int:pk>/update/',update_post.as_view(),name="update_post"),
    path('post/<int:pk>/delete/',delete_post.as_view(),name="delete_post"),
]