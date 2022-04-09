from rest_framework import generics
from django.db.models import F
from django.db.models.functions import Ln

from restaurantManager.models import Restaurant as RestaurantModel
from restaurantManager.serializers import RestaurantReadSerializer


# TODO: Swagger


class RestaurantDetail(generics.RetrieveAPIView):  # get detail of the restaurant
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantReadSerializer
    lookup_field = 'business_id'


class RestaurantList(generics.ListAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantReadSerializer

    def get_queryset(self):
        queryset = RestaurantModel.objects.all()
        category = self.request.query_params.get('category')
        if category:
            return queryset.filter(categories__name=category).annotate(ordering=F('stars') * Ln('review_cnt')).\
                order_by('-ordering')
        return queryset
