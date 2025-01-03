from . import views
from .views import LibraryDetailView
from .views import list_books
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import admin_view,librarian_view,member_view
urlpatterns = [
    path('all_books/',views.list_books,name='all_books'),
    path('all_books/',LibraryDetailView.as_view(),name='all_books'),
    path('signup/',views.register,name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='logout'),
    path('logout/',LogoutView.as_view(template_name='Alx_DjangoLearnLab/django-models/LibraryProject/relationship_app/login.html'),name='logout'),
    path('Admin_view/',admin_view.Admin,name='Admin_view'),
    path('Librarian_view/',librarian_view.librarian,name='Librarian_view'),
    path('Member_view/',member_view.member,name='Member_view'),
    path('add_book/',views.add_book_per,name='add_book_permission'),
    path('edit_book/',views.add_book_per,name='add_book_permission'),
    path('delete_book/',views.add_book_per,name='add_book_permission')
]
