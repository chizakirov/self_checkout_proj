from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt

from apps.login.models import * 
from apps.barcode_scanner.models import *

def main(request):
    return render(request, "login/main.html")

def register(request):
    error = User.objects.register_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect("/")
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'], email = request.POST['email'], password= hashed_pw)
        # messages.add_message(request, messages.INFO, "Successfully registered. Login to your account!", extra_tags = "registered")
        return redirect("/")


def login(request):
    if 'user_id' not in request.session:
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            user = User.objects.filter(email = request.POST['login_email'])
            request.session['first_name'] = user[0].first_name
            request.session['user_id'] = user[0].id
            return redirect('/scanner')
    else:
        return redirect('/scanner')


def clear(request):
    request.session.clear()
    return redirect("/")