from django.db import models, transaction
from django.core.validators import MaxValueValidator, MinValueValidator

from restaurantManager.models.base import BaseModel
from restaurantManager.models.user import User
from restaurantManager.models.restaurant import Restaurant



class Review(BaseModel):
    review_id = models.CharField(max_length=32, null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    stars = models.FloatField(null=False, validators=[MaxValueValidator(5), MinValueValidator(0)])
    useful = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    cool = models.IntegerField(default=0)
    text = models.CharField(max_length=5000, null=False)  # TODO: check we have only star reviews or not
    publish_date = models.DateTimeField(null=False)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.pk:  # create process
            self.user.add_stars(self.stars)
            self.restaurant.add_stars(self.stars)
            super().save(*args, **kwargs)
        else:  # update process
            pass
            # TODO: handle update review?
