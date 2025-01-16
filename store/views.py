from django.shortcuts import render
from .models import Order, Products
from dj_affiliate.models import Affiliate
from decimal import Decimal

def index(request):
    products = Products.objects.all()
    return render(request, "index.html", {"products": products})

def order(request):
    product_id = request.GET.get('product_id')
    order = Order.objects.create(user=request.user, product_id=product_id)
    affiliate_id = request.affiliate
    if affiliate_id:
        product_price = order.product.price
        affiliate = Affiliate.objects.get(affiliate_id=affiliate_id)
        reward_increment = product_price * Decimal('0.05')
        affiliate.reward_amount += reward_increment
        affiliate.save()
    return render(request, "order.html")