from rest_framework import serializers
from .models import *

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