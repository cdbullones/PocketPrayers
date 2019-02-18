from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prayers.views import PrayerViewSet


router = routers.DefaultRouter()
router.register(r'prayers', PrayerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
