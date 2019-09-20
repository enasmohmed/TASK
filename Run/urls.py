from django.conf.urls import url
from django.urls import re_path, path, include
from rest_framework import routers

import Run
from Run.views import  PersonViewSet

router = routers.DefaultRouter()
router.register('Run', PersonViewSet)
app_name = Run

urlpatterns = [
    url(r'^', include(router.urls)),
]
