from django.db import models
from apps.login.models import User
from apps.barcode_scanner.models import Product

class Cart(models.Model):
    order_quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits = 5, decimal_places = 2)
    products_added = models.ManyToManyField(Product, related_name = "products_in_cart")
    user_added = models.ForeignKey(User, related_name = "carts_of_user")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)