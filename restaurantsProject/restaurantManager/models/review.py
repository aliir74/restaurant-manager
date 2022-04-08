from django.db import models

from restaurantManager.models.base import BaseModel
from restaurantManager.models.user import User
from restaurantManager.models.restaurant import Restaurant


class Review(BaseModel):
    review_id = models.CharField(max_length=30, null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    stars = models.FloatField(default=0)
    useful = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    cool = models.IntegerField(default=0)
    text = models.CharField(max_length=300, null=False)  # TODO: check we have only star reviews or not
    publish_date = models.DateTimeField(null=False)
