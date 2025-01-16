from django.db import models
from django.conf import settings

class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product")

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)

