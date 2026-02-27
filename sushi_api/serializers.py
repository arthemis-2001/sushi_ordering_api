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

class OrderItemSerializer(serializers.ModelSerializer):
    sushi_id = serializers.PrimaryKeyRelatedField(
        queryset=Sushi.objects.all(),
        source="sushi",
        write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["sushi", "sushi_id", "quantity"]
        depth = 1
    
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value

class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        source="customer"
    )

    items = OrderItemSerializer(
        source="orderitem_set",
        many=True,
        read_only=True
    )

    new_items = OrderItemSerializer(
        many=True,
        write_only=True,
        required=False
    )

    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "customer_id", "created_at", "items", "new_items", "total_price"]

    def create(self, validated_data):
        items_data = validated_data.pop("new_items", [])
        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderItem.objects.create(order=order, **item)

        order.calculate_total()
        return order

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(
        source="order_set",
        many=True,
        read_only=True
    )

    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'address', 'orders']