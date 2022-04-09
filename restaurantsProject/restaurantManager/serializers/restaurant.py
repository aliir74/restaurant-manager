from rest_framework import serializers
from restaurantManager.models import Restaurant
from restaurantManager.serializers import BusinessHourSerializer, ReviewReadSerializer


class RestaurantReadSerializer(serializers.ModelSerializer):
    opening_hours = BusinessHourSerializer(read_only=True, many=True)
    reviews = ReviewReadSerializer(read_only=True, many=True)  # TODO: how to limit number of reverted elements?

    class Meta:
        model = Restaurant
        fields =['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars',
                 'review_cnt', 'is_open', 'attributes', 'reviews', 'categories', 'opening_hours']
