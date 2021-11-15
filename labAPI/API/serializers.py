from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# class userSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'username', 'password')
#
#     def save(self, **kwargs):
#         user = User(email=self.validated_data.get('email'), username=self.validated_data.get('username'),
#                     password=self.validated_data.get('password'))
#         user.save()
#         return User


class userSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = '__all__'


class seriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = series
        fields = '__all__'


class castSerializer(serializers.ModelSerializer):
    class Meta:
        model = cast
        fields = '__all__'


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
