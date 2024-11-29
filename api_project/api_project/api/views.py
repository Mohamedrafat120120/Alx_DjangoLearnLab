from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookList(generics.ListAPIView):
    data=Book.objects.all()
    
    serializer=BookSerializer(data,many=True)
    
    




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer   
    