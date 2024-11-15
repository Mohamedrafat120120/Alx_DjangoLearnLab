from . import views
from .views import LibraryDetailView
from .views import list_books
from .views import registeration
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('all_books',views.list_books,name='all_books'),
    path('all_books',LibraryDetailView.as_view(),name='all_books'),
    path('signup/',registeration.as_view(),name='signup'),
    path('login',LoginView.as_view(template_name='relationship_app/user_registration/login.html'),name='logout'),
    path('logout',LogoutView.as_view(),name='logout')
]
