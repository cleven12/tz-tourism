from django.urls import path
from .views import (
    attraction_list_create,
    attraction_detail,
    featured_attractions,
    attractions_by_category,
    attractions_by_region,
    endemic_species_list,
    attraction_boundary,
    attraction_boundary_geojson,
    attractions_within,
    attractions_nearby,
    citation_list,
    attraction_citations,
    endemic_species_citations,
)
from app.feedback.views import attraction_reviews

urlpatterns = [
    path('', attraction_list_create, name='attraction-list-create'),
    path('featured/', featured_attractions, name='attraction-featured'),
    path('by_category/', attractions_by_category, name='attraction-by-category'),
    path('by_region/', attractions_by_region, name='attraction-by-region'),
    path('within/', attractions_within, name='attractions-within'),
    path('nearby/', attractions_nearby, name='attractions-nearby'),
    path('citations/', citation_list, name='citation-list'),
    path('endemic-species/<int:pk>/citations/', endemic_species_citations, name='endemic-species-citations'),
    path('<slug:slug>/endemic-species/', endemic_species_list, name='attraction-endemic-species'),
    path('<slug:slug>/boundary/', attraction_boundary, name='attraction-boundary'),
    path('<slug:slug>/boundary/geojson/', attraction_boundary_geojson, name='attraction-boundary-geojson'),
    path('<slug:slug>/citations/', attraction_citations, name='attraction-citations'),
    path('<slug:slug>/reviews/', attraction_reviews, name='attraction-reviews'),
    path('<slug:slug>/', attraction_detail, name='attraction-detail'),
]
