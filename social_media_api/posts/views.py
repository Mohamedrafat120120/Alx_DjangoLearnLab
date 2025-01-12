from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status,permissions,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post,Comment,Like
from .serializers import post_serializer,comment_serializer,likeserializer
from rest_framework.authentication import TokenAuthentication
from accounts.models import CustomUser
from notifications.models import Notification
# Create your views here.
class view_posts(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset=Post.objects.all()
    serializer_class=post_serializer
    # def get_queryset(self):
    #     return Post.objects.filter(author=self.request.user)
    
    
class view_comments(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=comment_serializer
    queryset=Comment.objects.all()
    # def get_queryset(self):
    #     return Comment.objects.filter(author=self.request.user)
    
    
    
class edit_post(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=comment_serializer
    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    
    
    
class edit_comment(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=comment_serializer
    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    
    

class feed(APIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,user_id):
          user=request.user
          following_users=user.following.all()
          posts=Post.objects.filter(author__in=following_users).order_by('created_at')
          serialize=post_serializer(posts)
          return Response(serialize.data,status=status.HTTP_200_OK)
 
 
class like(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,pk):
        post=generics.get_object_or_404(Post, pk=pk)
        like=Like.objects.get_or_create(user=request.user, post=post)
        notify=Notification.objects.create()
        like_serializer=likeserializer(like,many=False)
        return Response(like_serializer.data,status=status.HTTP_200_OK)
    
    
    
    
    
    
    
    
    
    
        
        