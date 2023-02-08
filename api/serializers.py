from rest_framework import serializers
from accounts.models import ChatUser, Message

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatUser
        fields = ['username', 'is_staff']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'reciever', 'content', 'created_at']