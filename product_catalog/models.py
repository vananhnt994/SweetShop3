from django.db import models
from django.urls import reverse



# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    category_description = models.TextField()
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category_slug', args=(self.slug,))

class Product(models.Model):

    product_name= models.CharField(max_length=30,unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    product_old_price = models.DecimalField(max_digits=9,decimal_places=2)
    product_price = models.DecimalField(max_digits=9,decimal_places=2)
    product_size = models.CharField(max_length=20,default='small')
    product_sugar = models.DecimalField(max_digits=3,decimal_places=1)
    product_ice = models.CharField(max_length=20,default='regular')
    product_quantity = models.IntegerField()
    product_description = models.TextField()
    is_active= models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = "products"
        ordering = ['-created_at']

    def __unicdoe__(self):
        return self.product_name


    def get_absolute_url(self):
        return reverse('product_slug', args=(self.slug))

    def sale_price(self):
        if self.product_old_price > self.product_price:
            return self.product_price
        else:
            return None

