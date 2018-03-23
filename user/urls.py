from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'api', views.UserViewSet)

app_name = 'user'
urlpatterns = [
    path('new/user', views.create_user_page, name='create'),
    path('user/added', views.create_user, name='addUser'),
    path('login/', views.login_page, name='login'),
    path('welcome/', views.user_login, name='welcome'),

    ## REST URLS ##
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
