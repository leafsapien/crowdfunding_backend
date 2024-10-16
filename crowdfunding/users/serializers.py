from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'read_only': False}, #This will ensure username is read-only and can not be edited
                        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)