from django.shortcuts import render
from .models import MyUser
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import Token
from rest_framework.authentication import authenticate
# Create your views here.
class register(APIView):
    def post(self, request):
        if not MyUser.objects.filter(user=request.data['email']).exists:
            serializer = registerserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Massege':'Account Created','Data':serializer.data}, status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({'Massege':'Account Already Exists'}, status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'Massege':'Login Successfull','Token':token.key}, status=status.HTTP_200_OK)

class profile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        user = request.user
        serializer = profileserializer(user,many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)