from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Notification
from .serializers import *

# Create your views here.

class notify(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request,user_id):
        user=request.user
        notification=Notification.objects.create(rec)
