from django.shortcuts import get_object_or_404 
from rest_framework import generics 
from .models import *
from api.serializer import AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class Bookview(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer
    
class Bookviewlist(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class=AuthorSerializer
    
    
class Bookviewupdate(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset =Book.objects.get(pk=id)
    serializer_class=AuthorSerializer
    
    
class Bookviewdelete(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset = Book.objects.get(pk=id)
    serializer_class=AuthorSerializer
    
    