
from django.db import models
import uuid


class ProductDetail(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CustomerData(models.Model):
    item = models.ForeignKey(ProductDetail, on_delete= models.CASCADE)
    pieces = models.IntegerField(default=1)
     
    def _str_(self):
        return self.id

@property
def totalPrice(self):
    result = self.pieces*self.price
    return result