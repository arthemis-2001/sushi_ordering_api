from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Sushi(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    phone = PhoneNumberField(unique=True, region="US")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey("Customer", on_delete=models.PROTECT, related_name="orders")
    order_items = models.ManyToManyField("Sushi", through="OrderItem")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.PROTECT)
    sushi = models.ForeignKey("Sushi", on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.sushi.name}"
    