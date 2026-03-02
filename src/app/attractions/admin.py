from django.contrib import admin
from .models import Attraction, AttractionImage, AttractionTip, EndemicSpecies, AttractionBoundary, Citation


class AttractionImageInline(admin.TabularInline):
    model = AttractionImage
    extra = 1

class AttractionTipInline(admin.TabularInline):
    model = AttractionTip
    extra = 1

class EndemicSpeciesInline(admin.TabularInline):
    model = EndemicSpecies
    extra = 1

class AttractionBoundaryInline(admin.StackedInline):
    model = AttractionBoundary

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'category', 'difficulty_level', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'difficulty_level', 'region', 'is_featured', 'is_active']
    search_fields = ['name', 'description', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [AttractionImageInline, AttractionTipInline, EndemicSpeciesInline, AttractionBoundaryInline]
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'region', 'category', 'short_description', 'description', 'featured_image')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude', 'altitude', 'nearest_airport', 'distance_from_airport')
        }),
        ('Difficulty & Access', {
            'fields': ('difficulty_level', 'access_info', 'requires_guide', 'requires_permit')
        }),
        ('Timing & Fees', {
            'fields': ('best_time_to_visit', 'seasonal_availability', 'estimated_duration', 'entrance_fee')
        }),
        ('Metadata', {
            'fields': ('created_by', 'is_active', 'is_featured', 'created_at', 'updated_at')
        }),
    )


@admin.register(AttractionImage)
class AttractionImageAdmin(admin.ModelAdmin):
    list_display = ['attraction', 'caption', 'order', 'uploaded_at']
    list_filter = ['attraction']


@admin.register(AttractionTip)
class AttractionTipAdmin(admin.ModelAdmin):
    list_display = ['attraction', 'title', 'created_by', 'created_at']
    list_filter = ['attraction', 'created_at']


@admin.register(EndemicSpecies)
class EndemicSpeciesAdmin(admin.ModelAdmin):
    list_display = ['common_name', 'scientific_name', 'attraction', 'conservation_status', 'created_at']
    list_filter = ['conservation_status', 'attraction']
    search_fields = ['common_name', 'scientific_name']


@admin.register(Citation)
class CitationAdmin(admin.ModelAdmin):
    list_display = ['title', 'citation_type', 'year', 'is_primary_source']
    list_filter = ['citation_type', 'year', 'is_primary_source']
    search_fields = ['title', 'author', 'publisher']
    filter_horizontal = ['attractions', 'regions', 'endemic_species', 'articles']
