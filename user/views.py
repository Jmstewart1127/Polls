from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = UserSerializer(data=request.method)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        serializer = UserSerializer(data=request.method)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_user_page(request):
    return render(request, 'user/newuser.html')


def create_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password1 = request.POST['retype-password']
    if password == password1:
        u = User.objects.create_user(username=username, email=email, password=password, is_active=1)
        u.save()
        return render(request, 'polls/index.html')
    else:
        return render(request, 'user/newuser.html')


def login_page(request):
    return render(request, 'user/login.html')


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'user/welcome.html')
    else:
        EOFError('Invalid username or password')
