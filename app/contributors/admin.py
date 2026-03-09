from django.contrib import admin
from .models import CreatorProfile

@admin.register(CreatorProfile)
class CreatorProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'display_name', 'is_verified_creator', 'is_public', 'joined_at']
    list_filter = ['is_verified_creator', 'is_public', 'expertise']
    search_fields = ['username', 'display_name', 'user__email']
    readonly_fields = ['joined_at', 'updated_at']
