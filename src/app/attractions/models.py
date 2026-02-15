from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from app.regions.models import Region

User = get_user_model()


class Attraction(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
        ('difficult', 'Difficult'),
        ('extreme', 'Extreme'),
    ]

    CATEGORY_CHOICES = [
        ('mountain', 'Mountain'),
        ('beach', 'Beach'),
        ('wildlife', 'Wildlife Safari'),
        ('cultural', 'Cultural Site'),
        ('historical', 'Historical Site'),
        ('adventure', 'Adventure Activity'),
        ('national_park', 'National Park'),
        ('island', 'Island'),
        ('waterfall', 'Waterfall'),
        ('lake', 'Lake'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='attractions')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    
    # Location data
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.IntegerField(help_text='Altitude in meters', null=True, blank=True)
    
    # Difficulty & Access
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    access_info = models.TextField(help_text='How to reach this attraction')
    nearest_airport = models.CharField(max_length=100, blank=True)
    distance_from_airport = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text='Distance in km')
    
    # Seasonal info
    best_time_to_visit = models.CharField(max_length=200)
    seasonal_availability = models.TextField(help_text='When is this attraction accessible?')
    
    # Practical info
    estimated_duration = models.CharField(max_length=100, help_text='e.g., 5-7 days, 2 hours')
    entrance_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Fee in USD')
    requires_guide = models.BooleanField(default=False)
    requires_permit = models.BooleanField(default=False)
    
    # Media
    featured_image = CloudinaryField('image')
    
    # Metadata
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_attractions')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['region']),
            models.Index(fields=['difficulty_level']),
        ]

    def __str__(self):
        return self.name


class AttractionImage(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-uploaded_at']

    def __str__(self):
        return f"{self.attraction.name} - Image {self.order}"


class AttractionTip(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='tips')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.attraction.name} - {self.title}"
