from django.db import models

from restaurantManager.models.base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=60, null=False)
