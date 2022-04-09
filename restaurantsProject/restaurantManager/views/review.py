from rest_framework import generics
from rest_framework import mixins

from restaurantManager.models import Review as ReviewModel
from restaurantManager.serializers import ReviewWriteSerializer, ReviewReadSerializer


# TODO: Permission
# TODO: Swagger
# TODO: Pagination

class ReviewDetail(generics.RetrieveDestroyAPIView):
    queryset = ReviewModel.objects.all()
    read_serializer_class = ReviewReadSerializer
    write_serializer_class = ReviewWriteSerializer
    lookup_field = 'review_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return user.reviews.all()


class ReviewUserList(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = ReviewModel.objects.all()
    write_serializer_class = ReviewWriteSerializer
    read_serializer_class = ReviewReadSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return user.reviews.all()


class ReviewList(generics.ListAPIView):
    queryset = ReviewModel.objects.all()
    read_serializer_class = ReviewReadSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            return self.queryset.filter(text__contains=keyword)
        return self.queryset


class RestaurantReviews(generics.ListAPIView):  # get review of one restaurant
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewReadSerializer
    lookup_field = 'restaurant__business_id'
