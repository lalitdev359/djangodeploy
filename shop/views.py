from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def category(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'shop/index.html',context)

def products(request,slug):
    category=Category.objects.filter(slug=slug).first()
    products=Product.objects.filter(category=category)
    context={'products':products}
    return render(request,'shop/products.html',context)

