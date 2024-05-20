from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_screen(request):
    print(request.headers)
    return render(request, 'main.html', {})
