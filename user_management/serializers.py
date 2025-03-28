from rest_framework import serializers
from user_management.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
        