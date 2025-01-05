from .models import CustomUser
from rest_framework import serializers


class registerserializer(serializers.ModelSerializer):

    class Meta:
        model=CustomUser
        fields="__all__"
       
        
class loginserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email','password']
        
class profileserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"
        