from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    images = models.ImageField(upload_to='images/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.product_name
    
    
    def product_link(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
