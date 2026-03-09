from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from app.attractions.models import Attraction
from app.core.mixins import SEOMixin

User = get_user_model()


class Article(SEOMixin, models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.CharField(max_length=400, help_text='Short teaser shown on listing cards')
    content = models.TextField(help_text='Full article body (supports Markdown)')
    featured_image = CloudinaryField('image', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles')
    tags = models.CharField(
        max_length=200, blank=True,
        help_text='Comma-separated tags, e.g. "safari,wildlife,serengeti"'
    )
    related_attractions = models.ManyToManyField(
        Attraction, blank=True, related_name='blog_articles',
        help_text='Attractions mentioned or featured in this article'
    )
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['is_published']),
            models.Index(fields=['published_at']),
        ]

    def __str__(self):
        return self.title
