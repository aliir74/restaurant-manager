from django.db import models

from restaurantManager.models.base import BaseModel
from restaurantManager.models.category import Category


class Restaurant(BaseModel):
    business_id = models.CharField(max_length=32, null=False)
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)  # If we work only on Canada, We can add "Choices" to this field
    state = models.CharField(max_length=10, null=True)  # If we work only on Canada, We can add "Choices" to this field
    postal_code = models.CharField(max_length=16, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    stars = models.FloatField(default=0)
    review_cnt = models.IntegerField(default=0)
    is_open = models.BooleanField(default=0)
    attributes = models.JSONField(default=dict, null=True)
    categories = models.ManyToManyField(Category)

