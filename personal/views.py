from operator import attrgetter
from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse


def home_screen(request): 
    context = {}

    #If theres a GET request - searches for q then passes it to template
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    #Arranges newest posts at start/top of feed
    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts'] = blog_posts

    return render(request, 'personal/home.html', context)