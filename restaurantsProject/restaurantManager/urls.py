from django.urls import path
from restaurantManager.views import RestaurantDetail, ReviewDetail, ReviewList, RestaurantReviews, RestaurantList, \
    ReviewUserList

urlpatterns = [
    path('restaurant', RestaurantList.as_view(), name='restaurant-list'),
    path('restaurant/<str:business_id>/reviews', RestaurantReviews.as_view(), name='restaurant-reviews'),
    path('restaurant/<str:business_id>', RestaurantDetail.as_view(), name='restaurant-detail'),
    path('review', ReviewList.as_view(), name='review-list'),
    path('review/mine', ReviewUserList.as_view(), name='review-user'),
    path('review/<str:review_id>', ReviewDetail.as_view(), name='review-detail'),
]
