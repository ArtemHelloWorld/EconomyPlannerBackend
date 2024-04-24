from rest_framework import serializers
from users.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'job_title'
        ]


class UserSerializer(serializers.ModelSerializer):
    subordinates = ProfileSerializer(many=True, read_only=True)
    bosses = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'job_title',
            'subordinates',
            'bosses'
        ]

