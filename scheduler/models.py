from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ürün Adı")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Fotoğraf Yükle (Alternatif)")
    image_url = models.URLField(max_length=500, null=True, blank=True, verbose_name="Fotoğraf Linki (Önerilen)")

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
    notes = models.TextField(null=True, blank=True, verbose_name="Müşteri Notu")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.date} - {self.product.name} - {self.client_identifier}"
