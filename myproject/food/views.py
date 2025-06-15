import csv
import io
from django.shortcuts import redirect
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Dish, Restaurant, Order
from .serializers import DishSerializer, DishGroupedSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from users.models import Role
from rest_framework.pagination import LimitOffsetPagination



class DishesListView(generics.ListAPIView):
    queryset = Dish.objects.all().order_by('id')
    serializer_class = DishSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Dish.objects.all().order_by('id')
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.role != Role.ADMIN:
            return Response({"detail": "Only ADMIN can add dishes."}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DishCreateView(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != "ADMIN":
            raise PermissionDenied("Only admins can create dishes")
        serializer.save()

    def get(self, request, *args, **kwargs):
        dishes = Dish.objects.all().order_by('id')
        #restaurants = Restaurant.objects.prefetch_related("dish_set").all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(dishes, request, view = self)
        serializer = DishSerializer(page, many=True)

        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method == 'POST':

            return [permissions.IsAuthenticated()]
        return []





class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrdersListView(generics.ListAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Order.objects.all().order_by('id')
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status__icontains=status)
        return queryset

def import_dishes(request):

    if request.method != "POST":
        raise ValueError (f"Method {request.method} is not allowed")

    csv_file = request.FILES.get("file")
    if csv_file is None:
        raise ValueError("No csv file")

    data = csv_file.read().decode ("utf-8")
    reader = csv.DictReader(io.StringIO(data))
    total_created = 0
    total_updated = 0

    for row in reader:
        restaurant_name = row["restaurant"]
        dish_name = row["name"]
        dish_price = int(row["price"])

        try:
            rest = Restaurant.objects.get(name__icontains= restaurant_name.lower())
        except Restaurant.DoesNotExist:
            continue
        else:
            print(f"Restaurant {rest} found")


        dish, created = Dish.objects.update_or_create(
            name = dish_name,
            restaurant = rest,
            defaults ={"price": dish_price}
        )
        if created:
            total_created+=1
        else:
            total_updated+=1


    print(f"{total_created} dishes added and {total_updated} dishes updated")

    return redirect(request.META.get("HTTP_REFERER","/"))