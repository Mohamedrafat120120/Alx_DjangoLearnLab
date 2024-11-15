from . import views
from .views import LibraryDetailView,list_all_books
from django.urls import path
urlpatterns = [
    path('all_books',views.list_all_books,name='all_books'),
    path('all_books',LibraryDetailView.as_view(),name='all_books')
]
