from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Dish, Restaurant, Order
from .serializers import DishSerializer, DishGroupedSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from users.models import Role


class DishesListView(generics.ListAPIView):
    queryset = Restaurant.objects.prefetch_related("dish_set").all()
    serializer_class = DishGroupedSerializer
    permission_classes = [permissions.AllowAny]


class DishCreateView(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != "ADMIN":
            raise PermissionDenied("Only admins can create dishes")
        serializer.save()

    def get(self, request, *args, **kwargs):
        restaurants = Restaurant.objects.prefetch_related("dish_set").all()
        serializer = DishGroupedSerializer(restaurants, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method == 'POST':

            return [permissions.IsAuthenticated()]
        return []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.role != Role.ADMIN:
            return Response({"detail": "Only ADMIN can add dishes."}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
