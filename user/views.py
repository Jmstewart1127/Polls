from django.contrib.auth import authenticate, login
from django.shortcuts import render


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
