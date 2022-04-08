from django.db import models

from restaurantManager.models.base import BaseModel
from restaurantManager.models.restaurant import Restaurant


class BusinessHours(BaseModel):
    class Days(models.TextChoices):
        Mon = '1', 'Monday'
        Tue = '2', 'Tuesday'
        Wed = '3', 'Wednesday'
        Thu = '4', 'Thursday'
        Fri = '5', 'Friday'
        Sat = '6', 'Saturday'
        Sun = '7', 'Sunday'

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=Days.choices, null=False)
    open_time = models.TimeField(null=False)
    close_time = models.TimeField(null=False)
