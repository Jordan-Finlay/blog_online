from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_screen(request):
    context = {}
    context['tester_string'] = 'This is a test to input a string'

    return render(request, 'personal/home.html', context)