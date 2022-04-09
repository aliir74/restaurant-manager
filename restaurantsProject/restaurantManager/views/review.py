from rest_framework import generics
from rest_framework import mixins

from restaurantManager.models import Review as ReviewModel
from restaurantManager.serializers import Review as ReviewSerializer


# TODO: Permission
# TODO: Swagger


class ReviewDetail(generics.RetrieveDestroyAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'review_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return user.reviews.all()


class ReviewList(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return user.reviews.all()
