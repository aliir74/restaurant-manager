import math

from django.db import models, transaction
from django.core.validators import MaxValueValidator, MinValueValidator

from restaurantManager.models.base import BaseModel
from restaurantManager.models.category import Category


class Restaurant(BaseModel):
    business_id = models.CharField(max_length=32, null=False, unique=True)
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)  # If we work only on Canada, We can add "Choices" to this field
    state = models.CharField(max_length=10, null=True)  # If we work only on Canada, We can add "Choices" to this field
    postal_code = models.CharField(max_length=16, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    stars = models.FloatField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    review_cnt = models.IntegerField(default=0)
    is_open = models.BooleanField(default=0)
    attributes = models.JSONField(default=dict, null=True)
    categories = models.ManyToManyField(Category)

    @property
    def score(self):  # this formula used in category search restaurant order (it's duplicated and
        # you should change that in view file if you want)
        return self.stars*math.log(self.review_cnt)

    @transaction.atomic
    def add_stars(self, star):
        self.stars = ((self.stars * self.review_cnt) + star) / (self.review_cnt + 1)
        self.review_cnt += 1
        self.save()
