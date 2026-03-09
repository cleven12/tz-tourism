from django.urls import path
from .views import media_list_create, media_detail

urlpatterns = [
    path('', media_list_create, name='media-list'),
    path('<int:pk>/', media_detail, name='media-detail'),
]
