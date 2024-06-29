# inventory/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    company_name = models.CharField(max_length=255, unique=True)
    company_website = models.URLField()
    type_of_software = models.CharField(max_length=255)
    description = models.TextField()
    company_established = models.PositiveIntegerField()
    location_countries = models.TextField()
    location_cities = models.TextField()
    contact_telephone_no = models.CharField(max_length=50)
    address = models.TextField()
    no_of_employees = models.CharField(max_length=50)
    internal_professional_services = models.BooleanField(default=False)
    last_demo_date = models.DateField(null=True, blank=True)
    last_reviewed_date = models.DateField(null=True, blank=True)
    business_areas = models.TextField()
    modules = models.CharField(max_length=255)
    financial_services_client_types = models.CharField(max_length=255)
    cloud = models.CharField(max_length=255)
    additional_information = models.TextField(blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.company_name

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    similar_products = models.ManyToManyField('self', blank=True)
    document = models.FileField(upload_to='product_documents/', blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  

    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'

class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Rating by {self.user.username} on {self.product.name}'
