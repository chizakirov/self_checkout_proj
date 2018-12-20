from django.shortcuts import render, redirect
import numpy as np
import cv2 
import pyzbar.pyzbar as pyzbar
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Product


def root(request):
    return render(request, 'barcode_scanner/index.html')

def upload_code(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['name']
        fs = FileSystemStorage()
        name = fs.save('barcode', uploaded_file)
        url = fs.url(name)
        # print(name)
        context = {
        'url' : fs.url(name)
        }
        request.session['name'] = name
        print(url)
    return redirect('/scanner/read')

def read_barcode(request):
    img = cv2.imread('media/'+ request.session['name'], 0)
    try:
        decodedObjects = pyzbar.decode(img)
    except: 
        messages.error(request, "invalid image type")
        return redirect('/scanner')
    # print(img)
    # decodedObjects = request.GET['data']
    # print(decodedObjects)
    for obj in decodedObjects:
        try:
            id = Product.objects.get(sku = obj.data.decode()).id
            return redirect('/scanner/display/'+ str(id))
        except:
            messages.error(request, "SKU not Found")
    return redirect('/scanner')
        # print('Type : ', obj.type)
        # print('Data : ', obj.data,'\n')
        # print(obj.data.decode())
        # print(Product.objects.first().sku)
        # print(obj.data.decode() == Product.objects.first().sku)
        # print(Product.objects.get(sku = obj.data.decode()).id)
    # fs = FileSystemStorage(location = '/media')
    # fs.delete('barcode'

def display_page(request, id):
    context = {
        'item' : Product.objects.get(id = id)
    }
    return render(request, 'barcode_scanner/display_item.html',context)

def scanner(request):
    return render(request, 'barcode_scanner/scanner.html')

   