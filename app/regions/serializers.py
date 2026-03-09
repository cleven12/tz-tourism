from rest_framework import serializers
from .models import Region


class RegionSerializer(serializers.ModelSerializer):
    attraction_count = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'slug', 'description', 'image', 'latitude', 'longitude', 'attraction_count', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_attraction_count(self, obj):
        return obj.attractions.count()
