from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions


from restaurantManager.models import Review as ReviewModel
from restaurantManager.serializers import ReviewWriteSerializer, ReviewReadSerializer
from restaurantManager.permissions import IsOwnerOrReadOnly, IsOwner


# TODO: Swagger

class ReviewDetail(generics.RetrieveDestroyAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewReadSerializer
    lookup_field = 'review_id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ReviewUserList(mixins.CreateModelMixin, generics.ListAPIView):
    write_serializer_class = ReviewWriteSerializer
    read_serializer_class = ReviewReadSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return user.reviews.all()


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewReadSerializer

    def get_queryset(self):
        queryset = ReviewModel.objects.all()
        keyword = self.request.query_params.get('keyword')
        if keyword:
            return queryset.filter(text__contains=keyword)
        return queryset


class RestaurantReviews(generics.ListAPIView):  # get review of one restaurant
    serializer_class = ReviewReadSerializer

    def get_queryset(self):
        return ReviewModel.objects.filter(restaurant__business_id=self.kwargs['business_id'])
