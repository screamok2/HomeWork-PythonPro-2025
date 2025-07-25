from django.contrib import admin
from django.urls import path, include
from users.views import UserRegisterView
from food.views import DishesListView, DishCreateView, OrderCreateView
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('registration/', UserRegisterView.as_view(), name='user-register'),


]
