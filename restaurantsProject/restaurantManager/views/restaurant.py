from rest_framework import generics
from rest_framework import mixins

from restaurantManager.models import Restaurant as RestaurantModel
from restaurantManager.serializers import ReviewReadSerializer, RestaurantReadSerializer


# TODO: Permission
# TODO: Swagger


class RestaurantDetail(generics.RetrieveAPIView):  # get detail of the restaurant
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantReadSerializer
    lookup_field = 'business_id'
