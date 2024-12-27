from .models import MyUser
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class registerserializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields="__all__"
        def create(self, validated_data):
        # Use create_user to hash the password and create the user
          user = MyUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Create a token for the user
          Token.objects.create(user=user)
          return user
        
class loginserializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['email','password']
        
class profileserializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields="__all__"
        