from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_root, name="api-root"),
    path('sushis', views.SushiView.as_view(), name="sushi-list"),
    path('sushis/<int:pk>', views.SingleSushiView.as_view(), name="sushi-detail"),
]
