from rest_framework import serializers

from .models import MyApp


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyApp
        fields = '__all__'

