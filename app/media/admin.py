from django.contrib import admin
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type', 'is_approved', 'uploaded_by', 'created_at']
    list_filter = ['media_type', 'is_approved', 'license']
    search_fields = ['title', 'alt_text', 'caption', 'credit']
    readonly_fields = ['created_at', 'updated_at']
