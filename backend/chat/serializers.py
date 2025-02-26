from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['id', 'user', 'room_name', 'content', 'timestamp']
