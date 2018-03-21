from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.http import Http404
from django.template import loader
from django.urls import reverse
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


def show_create_question_page(request):
    return render(request, 'polls/create.html')


def create_question(request):
    question = request.POST['question']
    q = Question(question_text=question, pub_date=datetime.datetime.now())
    q.save()
    return HttpResponseRedirect('polls/addquestion.html')


def show_create_choices_page(request, question_id):
    return render(request, 'polls/addchoices.html')


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


def login_page(request):
    return render(request, 'polls/login.html')


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'polls/welcome.html')
    else:
        EOFError('Invalid username or password')
