from django.contrib import admin
from product_catalog.models import Product,Category
from product_catalog.forms import ProductAdminForm

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    #set values for how admin site lists the products
    list_display = ('product_name','product_price','product_old_price','product_sugar','product_size','product_ice','categories')
    list_display_links = ('product_name',)
    list_per_page = 50

    search_fields = ['product_name','product_description']
    exclude = ('product_name',)

    #sets up slug to be genereated from product name
    prepopulated_fields = {'slug':('product_name',)}

# registers product model with the admin site
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
     #sets up values for how admin site lists categories
     list_display = ('category_name',)
     list_display_links = ('category_name',)
     list_per_page = 20
     ordering = ['category_name']
     search_fields = ['category_name', 'category_description']

     # sets up slug to be generated from category name
     prepopulated_fields = {'slug' : ('category_name',)}

admin.site.register(Category, CategoryAdmin)


