from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
class BookSerializer(ModelSerializer.Serializer):
    class Meta:
        model = Book
        fields = '__all__'