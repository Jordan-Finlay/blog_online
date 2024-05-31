from django.shortcuts import render
from django.http import HttpResponse
from personal.models import Question

# Create your views here.

def home_screen(request): 
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, 'personal/home.html', context)