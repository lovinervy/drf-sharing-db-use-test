from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name='prices')
    price = models.DecimalField()
    date = models.DateField()

    def __str__(self) -> str:
        return f'{self.product}, price: {self.price}, per {self.date}'
