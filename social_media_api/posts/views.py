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
        return Post.objects.filter(author=self.request.user)
    
    
class view_comments(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=comment_serializer
    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    
    
    
class edit_post(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=comment_serializer
    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    
    
    
class edit_comment(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=comment_serializer
    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    
    

