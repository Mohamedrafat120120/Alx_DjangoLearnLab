from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookList(generics.ListAPIView):
    data=Book.objects.all()
    queryset = data
    serializer_class=BookSerializer