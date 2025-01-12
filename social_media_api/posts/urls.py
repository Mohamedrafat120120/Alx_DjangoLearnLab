from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'Post',view_posts)
comment_router=DefaultRouter()
comment_router.register(r'Commit',view_comments)
urlpatterns = [
    path('view-user-posts/',include(router.urls)),
    path('view-user-comments/',include(comment_router.urls)),
    path('feed/<int:user_id>/',feed.as_view(),name="feed"),
    path('<int:pk>/like/'),
    path('<int:pk>/unlike/'),
]
