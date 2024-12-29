from django.urls import path
from .views import *
urlpatterns = [
    path('view_posts/<int:user>/',view_posts.as_view() , name='view-user-posts'),
]
