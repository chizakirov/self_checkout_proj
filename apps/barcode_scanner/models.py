from django.db import models

# -Barcode Scanner
# 	-Product Models
# 		-name
# 		-sku
# 		-desc
# 		-price
# 	-Display Product(confirm)
# 	-/cart/add/<id>

class Product(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length = 255)
    desc = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    vendor = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 50)
    image = models.FileField(upload_to='product_pic')
    
    