from django.contrib import admin
from .models import Itinerary, ItineraryDay, ItineraryActivity


class ItineraryDayInline(admin.TabularInline):
    model = ItineraryDay
    extra = 1


class ItineraryActivityInline(admin.TabularInline):
    model = ItineraryActivity
    extra = 1


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_days', 'difficulty_level', 'is_public', 'created_by', 'created_at']
    list_filter = ['difficulty_level', 'is_public']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ItineraryDayInline]


@admin.register(ItineraryDay)
class ItineraryDayAdmin(admin.ModelAdmin):
    list_display = ['itinerary', 'day_number', 'title']
    inlines = [ItineraryActivityInline]
