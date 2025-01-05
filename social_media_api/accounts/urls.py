from django.urls import path
from .views import *
from .models import *
urlpatterns = [
    path('register/',register.as_view(),name='register'),
    path('login/',login.as_view(),name='login'),
    path('profile/',profile.as_view(),name='profile'),
    path('follow/<int:user_id>',follow_user.as_view(),name="follow_user"),
    path('unfollow/<str:user_id>/',unfollow_user.as_view(),name="unfollow_user")
    
]
