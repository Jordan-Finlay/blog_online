from django.shortcuts import render, redirect, get_object_or_404

from blog.models import BlogPost
from blog.forms import CreateBlogPostForm
from account.models import Account

def create_blog_view(request):

    context = {}
    
    user = request.user
    if not user.is_authenticated:#Checks if user is authenticated
        return redirect('must_authenticate')
    
    #Checks author, then saves and reloads
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, "blog/create_blog.html", context)


def detail_blog_view(request, slug):

    context = {}
    #Finds users post or sends to a 404 error
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)