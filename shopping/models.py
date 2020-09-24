from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class priceManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['price']) < 2:
            errors['price'] = "Price must be at least 2 decimal places"
        
        for price in Price.objects.all():
            if postData['price'] == price.price:
                errors['duplicate'] = "The price data already exists"
        
        return errors

class Price(models.Model):
    original_price = models.DecimalField(decimal_places=2, max_digits=5)
    product_id = models.OneToOneField(Product, related_name="price", null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = priceManager()

class Order(models.Model):
    quantity = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
