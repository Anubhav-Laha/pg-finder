from django.db import models

class Listing(models.Model):
    GENDER_CHOICES = [
        ('any', 'Any'),
        ('ladies', 'Ladies Only'),
        ('gents', 'Gents Only'),
    ]
    TYPE_CHOICES = [
        ('pg', 'PG'),
        ('hostel', 'Hostel'),
        ('coliving', 'Co-Living'),
    ]
    FOOD_CHOICES = [
        ('veg', 'Veg Only'),
        ('nonveg', 'Non-Veg'),
        ('both', 'Veg & Non-Veg'),
        ('none', 'No Food'),
    ]
    STAY_CHOICES = [
        ('1', '1 Month'),
        ('3', '3 Months'),
        ('6', '6 Months'),
        ('12', '12 Months'),
    ]
    title = models.CharField(max_length=200)
    pg_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='pg')
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=100, default='Navi Mumbai')
    distance_from_metro = models.CharField(max_length=100, blank=True)
    distance_from_college = models.CharField(max_length=100, blank=True)
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)
    security_deposit = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='any')
    has_single = models.BooleanField(default=False, verbose_name='Single Room')
    has_double = models.BooleanField(default=False, verbose_name='Double Room')
    has_triple = models.BooleanField(default=False, verbose_name='Triple Room')
    has_dormitory = models.BooleanField(default=False, verbose_name='Dormitory')
    food = models.CharField(max_length=20, choices=FOOD_CHOICES, default='none')
    minimum_stay = models.CharField(max_length=5, choices=STAY_CHOICES, default='1')
    amenities = models.TextField(blank=True)
    description = models.TextField(blank=True)
    owner_name = models.CharField(max_length=100, blank=True)
    owner_phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='listings/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, verbose_name='Show on Website')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title