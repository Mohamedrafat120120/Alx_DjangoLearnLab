from rest_framework import serializers
from .models import Notification

class notificationserializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'description', 'created_at')