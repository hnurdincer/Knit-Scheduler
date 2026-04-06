from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image', null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    CONTACT_CHOICES = [
        ('INSTA', 'Instagram'),
        ('TIKTOK', 'TikTok'),
        ('MAIL', 'Email'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    contact_type = models.CharField(max_length=10, choices=CONTACT_CHOICES)
    contact_handle = models.CharField(max_length=100)
    client_identifier = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.date}"
