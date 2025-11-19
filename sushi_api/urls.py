from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_root, name="api-root"),
    path('sushis', views.SushiView.as_view(), name="sushi-list"),
    path('sushis/<int:pk>', views.SingleSushiView.as_view(), name="sushi-detail"),
    path('customers', views.CustomerView.as_view(), name="customer-list"),
    path('customers/<int:pk>', views.SingleCustomerView.as_view(), name="customer-detail"),
    path('orders', views.OrderView.as_view(), name="order-list"),
    path('orders/<int:pk>', views.SingleOrderView.as_view(), name="order-detail"),
]
