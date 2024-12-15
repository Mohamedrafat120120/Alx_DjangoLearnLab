from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from .views import *


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('home/',home.as_view(),name="home"),
    path('posts/',posts.as_view(),name="posts"),
    path('display/',display.as_view(),name="display"),
    path('post/new/',display_create.as_view(),name="display_create"),
    path('display_detail/<int:pk>/',display_detail.as_view(),name="display_detail"),
    path('post/<int:pk>/update/',update_post.as_view(),name="update_post"),
    path('post/<int:pk>/delete/',delete_post.as_view(),name="delete_post"),
]