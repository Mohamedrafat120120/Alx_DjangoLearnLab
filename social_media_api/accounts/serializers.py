from .models import MyUser
from rest_framework import serializers

class registerserializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields="__all__"
        
class loginserializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['email','password']
        
class profileserializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields="__all__"
        