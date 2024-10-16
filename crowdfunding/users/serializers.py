from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'read_only': False}, #This will ensure username is read-only and can not be edited
                        }
#Checks that compulsory fields have been included during new User creation
    def validate(self, data):
        if self.instance is None: #If Instance is None, that means it's a POST method
            for field in ['username', 'first_name', 'last_name', 'email']:
                if not data.get(field):
                    raise serializers.ValidationError({field: f"{field} is required to create a new User"})
        return data
#Checks that the username is unique
    def validate_username(self, value):
        if self.instance: #If it's an instance then it's a PUT method
            if self.instance.username != value:
                raise serializers.ValidationError("Username can not be changed")
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("That Username already exists, please try another")
        return value
#Checks that the email address is unique, otherwise prompted to log in to existing account
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("That email address already exists in our system.  Please log in")
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
#Removes the username from the update data to ensure it doesn't get changed during PUT method update
    def update(self, instance, validated_data):
        validated_data.pop('username', None)
        return super().update(instance, validated_data)