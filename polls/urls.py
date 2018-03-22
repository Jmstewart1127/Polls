from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'choice', views.ChoiceViewSet)
router.register(r'question', views.QuestionViewSet)

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('questions/add/', views.show_create_question_page, name='addQuestion'),
    path('questions/created/', views.create_question, name='questionCreated'),
    path('questions/<int:question_id>/choices/added/', views.create_choice, name='choiceAdded'),

    ## REST URLS ##
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
