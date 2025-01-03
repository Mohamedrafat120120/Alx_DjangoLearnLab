from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from .models import MyUser
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import Token
# Create your views here.
class register(APIView):
    def post(self, request):
        serializer = registerserializer(data=request.data)
        if serializer.is_valid():
          if not MyUser.objects.filter(email=request.data['email']).exists():
                user=serializer.save()
                token= Token.objects.get_or_create(user=user)
                return Response({'Massege':'Account Created','Data':serializer.data,'Token':token}, status=status.HTTP_201_CREATED)
            
          else:
                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'Massege':'Account Already Exists'}, status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    def post(self, request):
        serialize=loginserializer(data=request.data)
        if serialize.is_valid():
           email=serialize.data.get('email')
           password=serialize.data.get('password')
           user = authenticate(username=email, password=password)
           if user:
               token= Token.objects.get_or_create(user=user)
               User=MyUser.objects.get(email=serialize.data.get('email'))
               user_serialize=profileserializer(User,many=False)
               return Response({'Massege':'Login Successfull',"user":user_serialize.data,'Token':token.key,}, status=status.HTTP_200_OK)
           else:
               return Response({"massege":"user not found"},status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class profile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        user = request.user
        serializer = profileserializer(user,many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
class follow_user(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request,user_id):
      target_user=get_object_or_404(MyUser,id=user_id)
      user=request.user
      if target_user != user and target_user not in user.following.all():
          user.following.add(target_user)
          return Response({"massege":"following success"},status=status.HTTP_202_ACCEPTED)
      return Response ({"massege":"you are already following other"},status=status.HTTP_400_BAD_REQUEST)   
  
       
class unfollow_user(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request,user_id):
      target_user=get_object_or_404(MyUser,id=user_id)
      user=request.user
      if  target_user  in user.following.all():
          user.following.remove(target_user)
          return Response({"massege":"unfollowing success"},status=status.HTTP_202_ACCEPTED)
      return Response ({"massege":"you are already unfollowing "},status=status.HTTP_400_BAD_REQUEST)        