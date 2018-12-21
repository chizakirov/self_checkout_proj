from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-copyZ]+$') 


class LoginManager(models.Manager):
    def register_validator(self, postData):
        error = {}
        if postData['first_name'] == "" and postData['last_name'] == "" and postData['email'] == "" and postData['password'] == "" :
            error['all'] = "All fields are required to register"
        if len(postData['first_name']) <2 or postData['first_name'].isalpha() == False:
            error['first_name'] = "First name must be at least 2 characters and contain only letters"
        if len(postData['last_name']) <2 or postData['last_name'].isalpha() == False:
            error['last_name'] = "Last name must be at least 2 characters and contain only letters"
        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = "Email address must be valid"
        if len(postData['password']) <8:
            error['password'] = "Password must be at least 8 characters"
        if len(postData['confirm_pw']) <8 or postData['confirm_pw'] != postData['password']:
            error['confirm_pw'] = "Confirm Password need to match"
        return error

    def login_validator(self,postData):
        errors = {}
        if postData['login_email'] == "" and postData['login_password'] == "" :
            errors['all'] = "Please enter email and password to login"
        elif not EMAIL_REGEX.match(postData['login_email']):
            errors['email_regex'] = "Email must be valid"
        elif not User.objects.filter(email = postData['login_email']):
            errors['email_exist'] = "This email hasn't been registered"
        elif len(postData['login_password']) < 8:
            errors['password_len'] = "Password must be at least 8 characters"
        elif not bcrypt.checkpw(postData['login_password'].encode(), User.objects.filter(email=postData['login_email'])[0].password.encode()):
            errors['password'] = "Please enter a correct password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = LoginManager()