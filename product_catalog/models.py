from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    category_description = models.TextField()
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category_slug', kwargs={'slug':self.slug})


    def get_products(self):

        return Product.objects.filter(slug=self.slug)

class Size(models.Model):

    size = models.CharField(max_length=20)

class Sugar(models.Model):

    sugar = models.DecimalField(max_digits=5, decimal_places=2)
class Ice(models.Model):
    ice = models.CharField(max_length=20)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    product_old_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_size = models.ForeignKey(Size,blank=True,on_delete=models.CASCADE)
    product_sugar = models.ForeignKey(Sugar,blank=True,on_delete=models.CASCADE)
    product_ice = models.ForeignKey(Ice,blank=True,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to='product_image',blank=True)
    product_description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    categories = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"
        ordering = ['-is_bestseller']


    def __unicode__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_slug', args={'slug':self.slug})

    def sale_price(self):
        if self.product_old_price > self.product_price:
            return self.product_price
        else:
            return None


