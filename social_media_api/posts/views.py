from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post,Comment
from .serializers import post_serializer,comment_serializer
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class view_posts(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=post_serializer
    def get_queryset(self):
        posts=self.kwargs.get(id)
        return post.objects.get(author=posts)
    
    
class view_posts(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=post_serializer
    def get_queryset(self):
        posts=self.kwargs.get('user')
        return Post.objects.get(author=posts)
    
    

