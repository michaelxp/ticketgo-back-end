from rest_framework import serializers
from users import models


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = instance.get_user_id()
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=16)
    password = serializers.CharField(max_length=16, write_only=True)