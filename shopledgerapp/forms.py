from django.forms import ModelForm, fields
from .models import ProductDetail,CustomerData,Customer

class productEntry(ModelForm):
    class Meta:
        model = ProductDetail
        fields = '__all__'
        
class dataEntry(ModelForm):
    class Meta:
        model = CustomerData
        fields = '__all__'

class customer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'