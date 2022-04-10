from rest_framework import serializers
from django.utils import timezone
import uuid

from restaurantManager.models import Review, Restaurant
from restaurantManager.serializers.limited_list import LimitedListSerializer


class ReviewWriteSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.CharField(required=True, write_only=True)
    review_id = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = Review
        fields = ['restaurant_id', 'stars', 'text', 'review_id']

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


class ReviewReadSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    restaurant_name = serializers.CharField(source='restaurant.name')

    class Meta:
        model = Review
        fields = ['review_id', 'username', 'restaurant_name', 'stars', 'text', 'useful', 'funny', 'cool',
                  'publish_date']


class ReviewReadSerializerLimited(ReviewReadSerializer):

    class Meta:
        list_serializer_class = LimitedListSerializer
        model = Review
        fields = ['review_id', 'username', 'restaurant_name', 'stars', 'text', 'useful', 'funny', 'cool',
                  'publish_date']
