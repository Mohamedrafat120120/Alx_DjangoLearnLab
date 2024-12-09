from rest_framework import serializers
from .models import *
import datetime
class BookSerializer(serializers.ModelSerializer):#nested serialization
        class Meta:
            model = Book
            fields = '__all__'
            
            def validate(self,data): # check if publication_year not in future
                if data['publication_year'] > datetime.date.today:
                    raise serializers.ValidationError('Publication year not valid')
                return data
class AuthorSerializer(serializers.ModelSerializer):
    book=BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'
   