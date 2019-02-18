from prayers.models import Prayer
from rest_framework import viewsets
from prayers.serializers import PrayerSerializer


class PrayerViewSet(viewsets.ModelViewSet):
    queryset = Prayer.objects.all()
    serializer_class = PrayerSerializer