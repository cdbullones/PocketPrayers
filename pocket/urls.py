from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prayers.views import PrayerViewSet
from pocket import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'prayers', PrayerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
