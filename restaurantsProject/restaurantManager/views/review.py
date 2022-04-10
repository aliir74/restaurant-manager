from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema

from restaurantManager.models import Review as ReviewModel
from restaurantManager.serializers import ReviewWriteSerializer, ReviewReadSerializer
from restaurantManager.permissions import IsOwnerOrReadOnly, IsOwner
from restaurantManager.api_docs.review import AddReview as AddReviewAPIDoc, DeleteReview as DeleteReviewAPIDoc,\
    GetReviewDetail as GetReviewDetailAPIDoc, GetMyReviews as GetMyReviewsAPIDoc, \
    GetAllReviews as GetAllReviewsAPIDoc, RestaurantReviews as RestaurantReviewsAPIDoc
from restaurantManager.api_docs import AuthenticationSchema


class ReviewDetail(generics.RetrieveDestroyAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewReadSerializer
    lookup_field = 'review_id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @swagger_auto_schema(manual_parameters=[GetReviewDetailAPIDoc.review_id_param],
                         responses=GetReviewDetailAPIDoc.RESPONSE_SCHEMA)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[AuthenticationSchema.auth_param, DeleteReviewAPIDoc.review_id_param],
                         responses=DeleteReviewAPIDoc.RESPONSE_SCHEMA)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReviewUserList(mixins.CreateModelMixin, generics.ListAPIView):
    write_serializer_class = ReviewWriteSerializer
    read_serializer_class = ReviewReadSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    @swagger_auto_schema(manual_parameters=[AuthenticationSchema.auth_param],
                         request_body=AddReviewAPIDoc.REQUEST_SCHEMA, responses=AddReviewAPIDoc.RESPONSE_SCHEMA)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[AuthenticationSchema.auth_param],
                         responses=GetMyReviewsAPIDoc.RESPONSE_SCHEMA)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return user.reviews.all()


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewReadSerializer

    @swagger_auto_schema(manual_parameters=[GetAllReviewsAPIDoc.keyword_param],
                         responses=GetAllReviewsAPIDoc.RESPONSE_SCHEMA)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = ReviewModel.objects.all()
        keyword = self.request.query_params.get('keyword')
        if keyword:
            return queryset.filter(text__contains=keyword)
        return queryset


class RestaurantReviews(generics.ListAPIView):
    serializer_class = ReviewReadSerializer

    @swagger_auto_schema(manual_parameters=[RestaurantReviewsAPIDoc.business_id_param],
                         responses=RestaurantReviewsAPIDoc.RESPONSE_SCHEMA)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return ReviewModel.objects.filter(restaurant__business_id=self.kwargs['business_id'])
