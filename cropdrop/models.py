from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Farmer Model
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Unknown Farmer")
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Product Model (ONLY ONE ✅)
class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name


# Customer Model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username


class Order(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()
    unit = models.CharField(max_length=20, default="kg")
    total_price = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    # CUSTOMER DETAILS (NEW FEATURE)
    name = models.CharField(max_length=100, default="N/A")
    phone = models.CharField(max_length=15, default="N/A")
    address = models.TextField(default="N/A")
    city = models.CharField(max_length=50, default="N/A")
    pincode = models.CharField(max_length=10, default="N/A")

    created_at = models.DateTimeField(default=timezone.now)

    # Optional (nice for admin panel)
    def __str__(self):
        return f"{self.product.name} - {self.customer.user.username} ({self.status})"





# Cart Model
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.customer.user.username} - {self.product.name}"