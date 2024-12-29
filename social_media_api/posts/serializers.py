from rest_framework import serializers
from .models import post,comment

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields ='__all__'
        
class comment_serializer(serializers.ModelField):
    post=post_serializer(many=True,read_only=True)
    class Meta:
        model = comment
        fields = '__all__'