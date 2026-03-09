from django.urls import path
from .views import article_list_create, article_detail

urlpatterns = [
    path('', article_list_create, name='article-list-create'),
    path('<slug:slug>/', article_detail, name='article-detail'),
]
