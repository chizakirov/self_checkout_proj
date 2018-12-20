from django.shortcuts import render, redirect
import numpy as np
import cv2 
import pyzbar.pyzbar as pyzbar
from django.core.files.storage import FileSystemStorage

def root(request):
    return render(request, 'barcode_scanner/index.html')

def upload_code(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['test']
        fs = FileSystemStorage()
        name = fs.save('barcode', uploaded_file)
        url = fs.url(name)
        # print(name)
        context = {
        'url' : fs.url(name)
        }
        request.session['name'] = name
        print(url)
    return redirect('/read')

def read_barcode(request):
    img = cv2.imread('media/'+ request.session['name'], 0)
    # print(img)
    # decodedObjects = request.GET['data']
    decodedObjects = pyzbar.decode(img)
    print(decodedObjects)
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')
    fs = FileSystemStorage(location = '/media')
    fs.delete('barcode')
    return redirect('/')

def scanner(request):
    return render(request, 'barcode_scanner/scanner.html')

   