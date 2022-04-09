from rest_framework import serializers
from django.utils import timezone
import uuid

from restaurantManager.models import Review, Restaurant


class ReviewSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.CharField(required=True)

    class Meta:
        model = Review
        fields = ['user', 'restaurant_id', 'stars', 'text']

    def create(self, validated_data):
        try:
            validated_data['restaurant'] = Restaurant.objects.get(business_id=validated_data['restaurant_id'])
            del validated_data['restaurant_id']
        except Restaurant.DoesNotExist:
            raise serializers.ValidationError({"detail": "This review can't be created. "
                                                         "The restaurant don't exist!"})
        validated_data['user'] = self.context['request'].user
        validated_data['publish_date'] = timezone.now()
        validated_data['review_id'] = uuid.uuid4().hex

        try:
            return Review.objects.create(**validated_data)
        except ValueError:
            raise serializers.ValidationError({"detail": "This review can't be created."})




