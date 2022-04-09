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


class RestaurantList(generics.ListAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantReadSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return self.queryset.filter(categories__name=category).extra(select={'score': 'stars * LN(review_cnt)'})\
                .extra(order_by=['-score'])
        return self.queryset
