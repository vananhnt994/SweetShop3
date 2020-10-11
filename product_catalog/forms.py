from django import forms
from product_catalog.models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','product_price','product_old_price')
    def clean_price(self):
        if self.cleaned_data['price']<=0:
            raise forms.ValidationError('Price must be greater than zero')
        return self.cleaned_data['price']