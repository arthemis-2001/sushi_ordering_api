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
    customer = models.ForeignKey("Customer", on_delete=models.PROTECT)
    order_items = models.ManyToManyField("Sushi", through="OrderItem")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Order #{self.id}"
    
    def calculate_total(self):
        total = sum(item.sushi.price * item.quantity for item in self.orderitem_set.all())
        self.total_price = total
        self.save()
        return total

class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    sushi = models.ForeignKey("Sushi", on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.sushi.name}"
    