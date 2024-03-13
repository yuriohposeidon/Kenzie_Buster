from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message= "email already registered.")])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default= None, required=False)
    is_employee = serializers.BooleanField(default=False)
    username = serializers.CharField(max_length=150, validators=[UniqueValidator(queryset=User.objects.all(), message= "username already taken.")])
    password = serializers.CharField(max_length=128, write_only=True)

    is_superuser = serializers.BooleanField(default=False, read_only=True)

    def create(self, validated_data):
        if validated_data["is_employee"]:
            user = User.objects.create_superuser(**validated_data)
        else: 
            user = User.objects.create_user(**validated_data)

        return user
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)