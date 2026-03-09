from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'excerpt', 'featured_image',
            'author_username', 'tags', 'published_at',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    related_attraction_slugs = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug', 'excerpt', 'content', 'featured_image',
            'author_username', 'tags', 'related_attraction_slugs',
            'is_published', 'published_at', 'created_at', 'updated_at',
        ]

    def get_related_attraction_slugs(self, obj):
        return list(obj.related_attractions.values_list('slug', flat=True))


class ArticleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title', 'slug', 'excerpt', 'content', 'featured_image',
            'tags', 'related_attractions', 'is_published', 'published_at',
        ]
