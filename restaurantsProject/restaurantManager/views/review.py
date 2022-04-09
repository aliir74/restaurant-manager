from rest_framework import generics
from rest_framework import mixins

from restaurantManager.models import Review as ReviewModel
from restaurantManager.serializers import Review as ReviewSerializer


class ReviewList(mixins.CreateModelMixin, generics.ListAPIView):
    # TODO: Permission
    queryset = ReviewModel.objects.all()
    # TODO: Swagger
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
