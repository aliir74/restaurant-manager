from rest_framework import serializers
from restaurantManager.models import BusinessHours


class BusinessHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHours
        fields = ['day', 'open_time', 'close_time']
