from . import views
from .views import LibraryDetailView
from .views import list_books
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import *
urlpatterns = [
    path('all_books/',views.list_books,name='all_books'),
    path('all_books/',LibraryDetailView.as_view(),name='all_books'),
    path('signup/',views.register,name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='logout'),
    path('logout/',LogoutView.as_view(template_name='Alx_DjangoLearnLab/django-models/LibraryProject/relationship_app/login.html'),name='logout'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('add_book/',views.add_book_per,name='add_book_permission'),
    path('edit_book/',views.add_book_per,name='add_book_permission'),
    path('delete_book/',views.add_book_per,name='add_book_permission')
]
