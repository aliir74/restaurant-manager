from django.db import models

from restaurantManager.models.base import BaseModel
from restaurantManager.models import User
from restaurantManager.models import Restaurant


class Review(BaseModel):
    review_id = models.CharField(max_length=30, null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    stars = models.FloatField(default=0)
    useful = models.BooleanField(default=0)
    funny = models.BooleanField(default=0)
    cool = models.BooleanField(default=0)
    text = models.CharField(max_length=300, null=False)  # TODO: check we have only star reviews or not
    publish_data = models.DateTimeField(null=False)
