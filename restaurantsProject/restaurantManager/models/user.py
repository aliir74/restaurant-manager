from django.db import models
from django.contrib.auth.models import User as DjangoUser

from restaurantManager.models.base import BaseModel


class User(DjangoUser, BaseModel):
    user_id = models.CharField(max_length=32, null=False)
    name = models.CharField(max_length=30, null=False)
    useful = models.IntegerField(default=0)
    average_stars = models.FloatField(default=0)
