from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
