from rest_framework import generics ,filters
from .models import *
from api.serializers import AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.views.generic import DetailView
from django_filters import rest_framework



# Create your views here.
class Bookviewlist(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class=AuthorSerializer
    
class Bookviewlist(DetailView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=AuthorSerializer
    
    
    def get_queryset(self):
        book_id = self.kwargs.get('pk')  # Extract 'pk' from URL
        return Book.objects.filter(pk=book_id)
    

    
class Bookview(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer
    
    
    
class Bookviewupdate(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset =Book.objects.all()
    serializer_class=AuthorSerializer
    
    
class Bookviewdelete(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class=AuthorSerializer
    
    
    
class Bookviewfilter(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=AuthorSerializer
    def get_queryset(self):
        book=self.kwargs.get('pk')
        return Book.objects.filter(pk=book)
    
    
class Bookviewsearching(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset=Book.objects.all()
    serializer_class=AuthorSerializer
    filter_backends= [filters.SearchFilter]
    search_fields=['title','author','publication_year']
    
    
class Bookviewordering(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset=Book.objects.all()
    serializer_class=AuthorSerializer
    filter_backends= [filters.OrderingFilter]
    ordering_fields=['title','author']
