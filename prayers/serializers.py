from prayers.models import Prayer
from rest_framework import serializers


class PrayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prayer
        fields = ('url', 'title', 'text', 'image', 'author', 'creation_date')
