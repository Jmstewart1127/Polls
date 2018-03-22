from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('welcome/', views.user_login, name='welcome'),
]
