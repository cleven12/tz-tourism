from django.contrib import admin
from .models import Attraction, AttractionImage, AttractionTip


class AttractionImageInline(admin.TabularInline):
    model = AttractionImage
    extra = 1


class AttractionTipInline(admin.TabularInline):
    model = AttractionTip
    extra = 1


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'category', 'difficulty_level', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'difficulty_level', 'region', 'is_featured', 'is_active']
    search_fields = ['name', 'description', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [AttractionImageInline, AttractionTipInline]
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
