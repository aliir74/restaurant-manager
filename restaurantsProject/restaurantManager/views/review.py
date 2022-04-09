from rest_framework import generics
from rest_framework import mixins

from restaurantManager.models import Review


class ReviewList(mixins.CreateModelMixin, generics.ListAPIView):
    # TODO: Permission
    queryset = Review.objects.all()
    # TODO: Swagger
    # TODO: Serializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
