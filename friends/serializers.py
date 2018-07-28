from rest_framework import serializers
from .models import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('name', 'age', 'email', 'address', 'created_at', 'updated_at')
