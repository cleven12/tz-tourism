from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttractionViewSet

router = DefaultRouter()
router.register(r'', AttractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
