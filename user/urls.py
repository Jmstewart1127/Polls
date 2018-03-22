from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('new/user', views.create_user_page, name='create'),
    path('user/added', views.create_user, name='addUser'),
    path('login/', views.login_page, name='login'),
    path('welcome/', views.user_login, name='welcome'),
]
