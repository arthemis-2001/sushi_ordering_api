from django.contrib import admin
from .models import Sushi, Customer, Order, OrderItem

# Register your models here.
admin.site.register(Sushi)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
