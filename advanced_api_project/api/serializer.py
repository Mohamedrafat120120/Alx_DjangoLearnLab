from rest_framework import serializers
from .models import *
import datetime
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    class BookSerializer(serializers.ModelSerializer):#nested serialization
        class Meta:
            model = Book
            fields = '__all__'
            
            def validate(self): # check if publication_year not in future
                if self.data['publication_year'] > datetime.date.today:
                    raise serializers.ValidationError('Publication year not valid')
                return True