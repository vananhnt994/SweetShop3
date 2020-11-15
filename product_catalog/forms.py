from django import forms
from product_catalog.models import Product, Category


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_price','product_old_price','slug','product_sugar','product_size','product_ice',
                  'categories','is_active','is_bestseller','product_image']

    product_name = forms.CharField(max_length=255)
    product_price = forms.DecimalField(max_digits=10,decimal_places=2)
    product_old_price = forms.DecimalField(max_digits=10,decimal_places=2)
    product_sugar = forms.CheckboxInput()
    product_size = forms.CheckboxInput()
    product_ice = forms.CheckboxInput()
    slug= forms.SlugField(max_length=255)
    categories = forms.CheckboxInput()
    is_active = forms.BooleanField()
    is_bestseller = forms.BooleanField()
    product_image= forms.ImageField()




    def clean_price(self):
        if self.cleaned_data['price']<=0:
            raise forms.ValidationError('Price must be greater than zero')
        return self.cleaned_data['price']

    # def __init__(self, *args, **kwargs):
    #
    #     super(ProductAdminForm, self).__init__(*args, **kwargs)
    #     self.fields["categories"].widget = forms.widgets.CheckboxInput()
    #     self.fields["categories"].help_text = ""
    #     self.fields["categories"].queryset = Category.objects.all()

class ProductListForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_image','product_name']

        product_name = forms.CharField(max_length=255)
        product_image = forms.ImageField()

class ProductShowForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_size','product_sugar','product_price']

        product_name = forms.CharField(max_length=255)
        product_size = forms.CharField(max_length=20)
        product_sugar = forms.DecimalField(max_digits=5,decimal_places=2)
        product_price = forms.DecimalField(max_digits=10,decimal_places=2)
