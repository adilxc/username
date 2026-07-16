from django.urls import path, include
from rest_framework import routers
from .views import nameview

router = routers.DefaultRouter()
router.register(r'names', nameview, basename='name')

urlpatterns = [
    path('', include(router.urls)),
]