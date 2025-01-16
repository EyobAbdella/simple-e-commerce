from django.shortcuts import render
from .models import Order, Products
from decimal import Decimal

def index(request):
    products = Products.objects.all()
    return render(request, "index.html", {"products": products})

def order(request):
    product_id = request.GET.get('product_id')
    order = Order.objects.create(user=request.user, product_id=product_id)
    return render(request, "order.html")