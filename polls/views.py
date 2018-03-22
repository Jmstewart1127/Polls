from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from rest_framework import viewsets
from polls.serializers import ChoiceSerializer, QuestionSerializer
from .models import Choice, Question, ChoiceSelected
from django.views import generic
import datetime


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def show_create_question_page(request):
    return render(request, 'polls/create.html')


def create_question(request):
    question = request.POST['question']
    q = Question(question_text=question, pub_date=datetime.datetime.now())
    q.save()
    return show_create_choices_page(request, q.id)


def show_create_choices_page(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/addchoices.html', {'question': question})


def create_choice(request, question_id):
    choice = request.POST['choice']
    question = get_object_or_404(Question, pk=question_id)
    c = Choice(question=question, choice_text=choice, votes=0)
    c.save()
    return render(request, 'polls/addchoices.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#