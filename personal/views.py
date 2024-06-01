from django.shortcuts import render
from account.models import Account
from django.http import HttpResponse


def home_screen(request): 
    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'personal/home.html', context)