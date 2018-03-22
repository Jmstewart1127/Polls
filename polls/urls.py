from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('questions/add/', views.show_create_question_page, name='addQuestion'),
    path('questions/created/', views.create_question, name='questionCreated'),
    # path('questions/<int:pk>/choices/add/', views.show_create_choices_page, name='addChoices'),
    path('questions/<int:question_id>/choices/added/', views.create_choice, name='choiceAdded'),

]
