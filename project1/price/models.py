from collections.abc import Iterable
from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True
    project_from = models.CharField(max_length=100, null=True, blank=True)
    local_id = models.PositiveIntegerField(null=True, blank=True)
    share_id = models.PositiveIntegerField(null=True, blank=True)


class Product(BaseModel):
    class Meta:
        pass
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class ProductPrice(BaseModel):
    product = models.ForeignKey(to=Product, related_name='prices', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self) -> str:
        return f'{self.product}, price: {self.price}, per {self.date}'
