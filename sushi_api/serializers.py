from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator 
from .models import Sushi, Customer, Order, OrderItem


class SushiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sushi
        fields = ['id', 'name', 'price']
        extra_kwargs = {
            'price': {'min_value': 0}
        }

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'address']

class OrderItemSerializer(serializers.ModelSerializer):
    sushi_id = serializers.IntegerField(source="sushi.id", read_only=True)
    sushi = serializers.PrimaryKeyRelatedField(
        queryset=Sushi.objects.all(),
        write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["sushi", "sushi_id", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        source="customer",
        queryset=Customer.objects.all()
    )

    items = OrderItemSerializer(
        source="orderitem_set",
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = ["id", "customer_id", "created_at", "items"]
