from .models import Sushi, Customer, Order, OrderItem
from .serializers import SushiSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
class SushiView(generics.ListCreateAPIView):
    queryset = Sushi.objects.all()
    serializer_class = SushiSerializer
    ordering_fields = ['name', 'price']
    filterset_fields = ['name', 'price']
    search_fields = ['name']

class SingleSushiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sushi.objects.all()
    serializer_class = SushiSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "sushi": reverse("sushi-list", request=request, format=format),
        # "customer": reverse("customer-list", request=request, format=format),
        # "orders": reverse("order-list", request=request, format=format)
    })
