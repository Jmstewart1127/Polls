from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class ChoiceSelected(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    selection_made = models.BooleanField(False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
