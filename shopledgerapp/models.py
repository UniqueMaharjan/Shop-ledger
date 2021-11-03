
from django.db import models
from django.db.models.fields.related import ForeignKey

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True,blank=False)
    

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    
    
    @property
    def get_product_total(self):
        items = self.customerdata_set.all()
        total = sum([item.get_total for item in items])
        return total

class CustomerData(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True,blank=True)
    item = models.ForeignKey(ProductDetail, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0)
     
    def _str_(self):
        return self.id
    @property
    def get_total(self):
        total = self.item.price*self.quantity
        return total
