from django.urls import path
from .views import *

urlpatterns = [
    path('Book_view/',Bookview.as_view(),name='Book_list'),
    path('Book/<int:pk>',Bookviewdetail.as_view(),name='Book_detail'),
    path('Book_list',Bookviewlist.as_view(),name='Book_list'),
    path('Book_update/',Bookviewupdate.as_view(),name='Book_update'),
    path('Book_delete/',Bookviewdelete.as_view(),name='Book_delete'),
    path('Book_filter/',Bookviewfilter.as_view(),name='Book_filter'),
    path('Book_searching/',Bookviewsearching.as_view(),name='Book_searching'),
    path('Book_ordering/',Bookviewordering.as_view(),name='Book_ordering'),
]
