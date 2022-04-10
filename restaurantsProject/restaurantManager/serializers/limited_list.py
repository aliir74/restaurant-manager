from abc import ABC

from rest_framework import serializers
from django.conf import settings


class LimitedListSerializer(serializers.ListSerializer, ABC):

    def to_representation(self, data):
        data = data.all()[:settings.LIMITED_RESULT_NUMBER]
        return super().to_representation(data)
