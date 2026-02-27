from .models import Sushi, Customer, Order
from .serializers import SushiSerializer, CustomerSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Create your views here.
class SushiView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Sushi.objects.all()
    serializer_class = SushiSerializer
    ordering_fields = ['name', 'price']
    filterset_fields = ['name', 'price']
    search_fields = ['name']


class SingleSushiView(generics.RetrieveUpdateDestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Sushi.objects.all()
    serializer_class = SushiSerializer


class CustomerView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Customer.objects.prefetch_related(
        "order_set",
        "order_set__orderitem_set",
        "order_set__orderitem_set__sushi"
    )
    serializer_class = CustomerSerializer
    ordering_fields = ['name', 'email', 'phone', 'address']
    filterset_fields = ['name', 'email', 'phone', 'address']
    search_fields = ['name', 'email', 'address']


class SingleCustomerView(generics.RetrieveUpdateDestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Customer.objects.prefetch_related(
        "order_set",
        "order_set__orderitem_set",
        "order_set__orderitem_set__sushi"
    )
    serializer_class = CustomerSerializer


class OrderView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Order.objects.prefetch_related(
        "orderitem_set",
        "orderitem_set__sushi"
    )
    serializer_class = OrderSerializer
    ordering_fields = ['created_at']
    filterset_fields = ['customer']
    search_fields = ['customer__name']


class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Order.objects.prefetch_related(
        "orderitem_set",
        "orderitem_set__sushi"
    )
    serializer_class = OrderSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "sushi": reverse("sushi-list", request=request, format=format),
        "customer": reverse("customer-list", request=request, format=format),
        "orders": reverse("order-list", request=request, format=format)
    })
