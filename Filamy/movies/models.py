from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    vendor = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=20.00)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    txn_id = models.CharField(max_length=200, null=True)

    location = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    movie = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='orderitem', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)




