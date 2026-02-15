from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.cache import cache
from .models import Attraction
from .serializers import (
    AttractionListSerializer, 
    AttractionDetailSerializer,
    AttractionCreateUpdateSerializer
)


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.filter(is_active=True).select_related('region', 'created_by').prefetch_related('images', 'tips')
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'short_description', 'region__name']
    ordering_fields = ['created_at', 'name', 'difficulty_level']

    def get_serializer_class(self):
        if self.action == 'list':
            return AttractionListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return AttractionCreateUpdateSerializer
        return AttractionDetailSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        cache_key = 'featured_attractions'
        featured = cache.get(cache_key)
        
        if not featured:
            featured = self.queryset.filter(is_featured=True)[:6]
            serializer = self.get_serializer(featured, many=True)
            cache.set(cache_key, serializer.data, 3600)
            return Response(serializer.data)
        
        return Response(featured)

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get('category')
        if not category:
            return Response({'error': 'Category parameter is required'}, status=400)
        
        attractions = self.queryset.filter(category=category)
        serializer = self.get_serializer(attractions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_region(self, request):
        region_slug = request.query_params.get('region')
        if not region_slug:
            return Response({'error': 'Region parameter is required'}, status=400)
        
        attractions = self.queryset.filter(region__slug=region_slug)
        serializer = self.get_serializer(attractions, many=True)
        return Response(serializer.data)
