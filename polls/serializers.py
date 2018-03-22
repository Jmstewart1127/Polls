from .models import Choice, Question
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text')


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):

    question = QuestionSerializer()

    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')

