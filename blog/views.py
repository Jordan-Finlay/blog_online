from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from blog.models import BlogPost
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account


#A function to create a post
def create_blog_view(request):

    context = {}

    #Checks if user is authenticated
    user = request.user
    if not user.is_authenticated:
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


#A function to see users posts
def detail_blog_view(request, slug):

    context = {}
    #Finds users post or sends to a 404 error
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)


#An edit post function(if the post belongs to user)
def edit_blog_view(request, slug):

    context = {}

    #Checks if the user is authenticated before editing post
    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    #Updates and shows a success message
    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj

    #The user can only update title/body or images
    form = UpdateBlogPostForm(
        initial = {
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image,
        }
    )

    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)


#A search bar function finding set then converting into a list
def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        #Searches posts and finds only unique
        posts = BlogPost.objects.filter(
            Q(title__icontains=q) |
            Q(body__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)
    
    return list(set(queryset))