from django.db import models
from django.contrib.gis.db import models as gis_models

from restaurantManager.models.base import BaseModel
from restaurantManager.models.category import Category


class Restaurant(BaseModel):
    business_id = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)  # If we work only on Canada, We can add "Choices" to this field
    state = models.CharField(max_length=10, null=True)  # If we work only on Canada, We can add "Choices" to this field
    postal_code = models.CharField(max_length=16, null=True)
    location = gis_models.PointField(null=True)
    stars = models.FloatField(default=0)
    review_cnt = models.IntegerField(default=0)
    is_open = models.BooleanField(default=0)
    attributes = models.JSONField(default={})
    categories = models.ManyToManyField(Category)

