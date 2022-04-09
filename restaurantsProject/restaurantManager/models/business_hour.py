from django.db import models

from restaurantManager.models.base import BaseModel
from restaurantManager.models.restaurant import Restaurant


class BusinessHours(BaseModel):
    class Days(models.TextChoices):
        Mon = 'Mon', 'Monday'
        Tue = 'Tue', 'Tuesday'
        Wed = 'Wed', 'Wednesday'
        Thu = 'Thu', 'Thursday'
        Fri = 'Fri', 'Friday'
        Sat = 'Sat', 'Saturday'
        Sun = 'Sun', 'Sunday'

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="business_hours")
    day = models.CharField(max_length=10, choices=Days.choices, null=False)
    open_time = models.TimeField(null=False)
    close_time = models.TimeField(null=False)
