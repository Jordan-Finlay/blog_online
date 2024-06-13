from operator import attrgetter
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import BlogPost
from blog.views import get_blog_queryset
from django.http import HttpResponse


BLOG_POSTS_PER_PAGE = 3


def home_screen(request): 
    context = {}

    #If theres a GET request - searches for q then passes it to template
    query = ""
    if request.GET:
        query = request.GET.get('q', "")
        context['query'] = str(query)

    #Arranges newest posts at start/top of feed
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts'] = blog_posts


    #pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, 'personal/home.html', context)