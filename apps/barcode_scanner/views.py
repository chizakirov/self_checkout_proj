from django.shortcuts import render, redirect
import numpy as np
import cv2 
import pyzbar.pyzbar as pyzbar
from django.core.files.storage import FileSystemStorage

def root(request):
    return render(request, 'barcode_scanner/index.html')

def upload_file(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['test']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print("name is", name)
        print("ULFN name is", uploaded_file.name)
        print(uploaded_file.size)
        print("url is", url)
        context['url'] = fs.url(name)
        request.session['name'] = name
    return redirect('/read')

def read_barcode(request):
    img = cv2.imread('media/' + request.session['name'], 0)
    # print('media/'+request.session['name'])
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(img)
    print(decodedObjects)
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')
     
    return redirect('/')

    