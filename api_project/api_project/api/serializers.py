from rest_framework import serializers
from .models import *
class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = '__all__'