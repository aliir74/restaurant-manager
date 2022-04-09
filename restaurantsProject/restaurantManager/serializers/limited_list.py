from abc import ABC

from rest_framework import serializers


class LimitedListSerializer(serializers.ListSerializer, ABC):

    def to_representation(self, data):
        data = data.all()[:5]
        return super().to_representation(data)
