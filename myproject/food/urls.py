from django.urls import path
from .views import DishCreateView, OrderCreateView

urlpatterns = [
    path("dishes/", DishCreateView.as_view(), name="dish-list-create"),
    path("orders/", OrderCreateView.as_view(), name="order-create"),
]
