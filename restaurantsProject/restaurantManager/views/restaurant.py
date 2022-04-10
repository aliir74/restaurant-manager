from rest_framework import generics
from django.db.models import F
from django.db.models.functions import Ln
from drf_yasg.utils import swagger_auto_schema

from restaurantManager.models import Restaurant as RestaurantModel
from restaurantManager.serializers import RestaurantReadSerializer
from restaurantManager.api_docs.restaurant import GetRestaurantDetail as GetRestaurantDetailAPIDoc, \
    GetAllRestaurant as GetAllRestaurantAPIDoc


class RestaurantDetail(generics.RetrieveAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantReadSerializer
    lookup_field = 'business_id'

    @swagger_auto_schema(manual_parameters=[GetRestaurantDetailAPIDoc.business_id_param],
                         responses=GetRestaurantDetailAPIDoc.RESPONSE_SCHEMA)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RestaurantList(generics.ListAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantReadSerializer

    @swagger_auto_schema(manual_parameters=[GetAllRestaurantAPIDoc.category_param],
                         responses=GetAllRestaurantAPIDoc.RESPONSE_SCHEMA)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = RestaurantModel.objects.all()
        category = self.request.query_params.get('category')
        if category:
            return queryset.filter(categories__name=category).annotate(ordering=F('stars') * Ln('review_cnt')).\
                order_by('-ordering')
        return queryset
