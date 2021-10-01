from django.forms import ModelForm, fields
from .models import ProductDetail,CustomerData

class productEntry(ModelForm):
    class Meta:
        model = ProductDetail
        fields = '__all__'
        
class dataEntry(ModelForm):
    class Meta:
        model = CustomerData
        fields = '__all__'