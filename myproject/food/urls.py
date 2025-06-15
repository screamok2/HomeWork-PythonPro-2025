from django.urls import path
from .views import DishCreateView, OrderCreateView, DishesListView, import_dishes
from .views import OrdersListView

urlpatterns = [
    path("dishes/", DishesListView.as_view(), name="dish-list-create"),
    path("orders/", OrderCreateView.as_view(), name="order-create"),
    path("admin/food/dish/import-dishes/", import_dishes, name="import_dishes"),
    path("food/orders/all/", OrdersListView.as_view(), name="order-list"),
]

