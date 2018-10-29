from rest_framework import serializers
from users.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True,max_length=32)

    class Meta:
        model = User
        fields = ('email', 'password',)


