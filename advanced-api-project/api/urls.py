from django.urls import path
from .views import *

urlpatterns = [
    path('books/',Bookviewlist.as_view(),name='Book_list'),
    path('Book/<int:pk>',Bookviewdetaillist.as_view(),name='Book_detail'),
    path('books/create',Bookcreateview.as_view(),name='Book_list'),
    path('books/update',Bookviewupdate.as_view(),name='Book_update'),
    path('books/delete',Bookviewdelete.as_view(),name='Book_delete'),
    path('Book_filter/',Bookviewfilter.as_view(),name='Book_filter'),
    path('Book_searching/',Bookviewsearching.as_view(),name='Book_searching'),
    path('Book_ordering/',Bookviewordering.as_view(),name='Book_ordering'),
]
