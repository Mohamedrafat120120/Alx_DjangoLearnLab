from rest_framework import serializers
from .models import Post,Comment

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'
        
class comment_serializer(serializers.ModelField):
    post=post_serializer(many=True,read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        
        
