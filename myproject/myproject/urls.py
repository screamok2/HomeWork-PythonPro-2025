from django.contrib import admin
from django.urls import path, include
from users.views import UserRegisterView, activate_user
from food.views import DishesListView, DishCreateView, OrderCreateView, OrdersListView, import_dishes
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("admin/food/dish/import-dishes/", import_dishes, name="import_dishes"),
    path('food/', include('food.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('registration/', UserRegisterView.as_view(), name='user-register'),
    path("activate/<uuid:code>/", activate_user, name="activate-user"),
    path('food/dishes/', DishesListView.as_view(), name='dishes-list'),
    path('food/dishes/', DishCreateView.as_view(), name='dishes-list'),
    path("orders/", OrderCreateView.as_view(), name="order-create"),
    path("food/orders/all/", OrdersListView.as_view(), name="order-list"),

]
