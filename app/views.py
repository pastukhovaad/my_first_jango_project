from django.shortcuts import render
from app.models import Product, Brand, Category


def index(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    context = {
        "products": products,
        "brands": brands,
        "categories": categories,
    }

    return render(request, "app/index.html", context=context)