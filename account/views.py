from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from blog.models import BlogPost

#Display of registration_view
def registration_view(request):
    context = {}
    if request.POST:
        #A form for registering checking email and password
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

#Display of logout
def logout_view(request):
    logout(request)
    return redirect('home')

#Display of login
def login_view(request):

    context = {}
    #A check if user is authenticated and sends them to home if not
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    #A post request for email and password
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()
    #Returns account form
    context['login_form'] = form
    return render(request, 'account/login.html', context)



def account_view(request):
    #Depending if user is currently logged in they can change account details
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    #Checks form and user is correct
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            #Updates with success message and saves form
            form.save()
            context['success_message'] = "Updated!"
    else:
        form = AccountUpdateForm(
            initial= {
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts

    return render(request, 'account/account.html', context)

def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})