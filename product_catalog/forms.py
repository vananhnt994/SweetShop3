from django import forms
from product_catalog.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_price','product_old_price','slug',
                  'categories','is_active','is_bestseller','product_image']
        widgets = {
            'categories': forms.CheckboxInput()
        }

    product_name = forms.CharField(max_length=255)
    product_price = forms.DecimalField(max_digits=10,decimal_places=2)
    product_old_price= forms.DecimalField(max_digits=10,decimal_places=2)
    slug= forms.SlugField(max_length=255)
    categories = forms.CheckboxSelectMultiple()
    is_active = forms.BooleanField()
    is_bestseller = forms.BooleanField()
    product_image= forms.ImageField()




    def clean_price(self):
        if self.cleaned_data['price']<=0:
            raise forms.ValidationError('Price must be greater than zero')
        return self.cleaned_data['price']

    def __init__(self, *args, **kwargs):

        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["categories"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["categories"].help_text = ""
        self.fields["categories"].queryset = Category.objects.all()
