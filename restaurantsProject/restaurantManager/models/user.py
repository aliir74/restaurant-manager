from django.db import models, transaction
from django.contrib.auth.models import User as DjangoUser

from restaurantManager.models.base import BaseModel


class User(DjangoUser, BaseModel):
    user_id = models.CharField(max_length=32, null=False)
    name = models.CharField(max_length=30, null=False)
    useful = models.IntegerField(default=0)
    average_stars = models.FloatField(default=0)
    stars_cnt = models.IntegerField(default=0)  # TODO: migration and fill others data

    @transaction.atomic
    def add_stars(self, star):
        self.average_stars = ((self.average_stars*self.stars_cnt)+star)/(self.stars_cnt+1)
        self.stars_cnt += 1
        self.save()
