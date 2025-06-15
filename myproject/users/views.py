from django.shortcuts import render, redirect
from django.views import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from django.views.decorators.csrf import csrf_exempt


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):

        data = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
        }
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'errors': serializer.errors})
