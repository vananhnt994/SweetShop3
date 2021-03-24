from product_catalog.models import Product, Category
from django.shortcuts import render
from django.views.generic.list import ListView



# Create your views here.
class ProductListView(ListView):
    model = Product

    def drink_list(request):

        categories = Category.objects.get(slug="drink")
        products = Product.objects.filter(categories_id=1)[:12]
        besteller = products[:3]

        return render(request,
                      'product_catalog/drink_list.html',
                      {'categories': categories,
                       'bestseller': besteller,
                       'products': products})

    def cake_list(request):

        categories = Category.objects.get(slug="cake")
        products = Product.objects.filter(categories_id=2)[:12]
        besteller = products[:3]

        return render(request,
                      'product_catalog/cake_list.html',
                      {'categories': categories,
                       'bestseller': besteller,
                       'products': products})
