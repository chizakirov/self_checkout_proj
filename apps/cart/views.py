from django.shortcuts import render, redirect
import numpy as np
import cv2 
import pyzbar.pyzbar as pyzbar
from django.core.files.storage import FileSystemStorage
from apps.login.models import User
from apps.barcode_scanner.models import Product
from apps.cart.models import Cart

def process_order(request):
    if 'grand_total' not in request.session:
        request.session['grand_total'] = 0
    else: 
        quantity = int(request.POST['order_quantity'])
        price = float(request.POST['price'])
        amount = quantity * price
        request.session['grand_total'] += amount
        product = Product.objects.get(sku = request.POST['sku'])
        user= User.objects.get(id=request.session['user_id'])
        new_cart = Cart.objects.create(order_quantity = quantity, subtotal = amount, user_added = user)
        new_cart.products_added.add(product)
        new_cart.save()
    return redirect('/cart/order_review')

def order_review(request):
    context = {
        'user_name': request.session['first_name'],
        'items': Cart.objects.all().values(),
        # 'products': Product.objects.
    }
    return render(request, "cart/order_review.html", context)

def delete(request,id):
    order = Cart.objects.get(id = id)
    order.delete()
    return redirect('/cart/order_review')

def checkout_process(request):
    context = {
        'user_name': request.session['first_name'],
        'amount': request.session['grand_total'],
    }
    return render(request,'cart/checkout.html', context)