from rest_framework import serializers
from restaurantManager.models import Restaurant
from restaurantManager.serializers.business_hour import BusinessHourSerializer
from restaurantManager.serializers.review import ReviewReadSerializerLimited
from restaurantManager.serializers.category import CategorySerializer


class RestaurantReadSerializer(serializers.ModelSerializer):
    business_hours = BusinessHourSerializer(read_only=True, many=True)
    reviews = ReviewReadSerializerLimited(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Restaurant
        fields = ['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars',
                  'review_cnt', 'is_open', 'attributes', 'reviews', 'categories', 'business_hours']
