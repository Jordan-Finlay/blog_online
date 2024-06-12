from django.urls import path
from blog.views import (

    create_blog_view,
    detail_blog_view,
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),#Sends user to create post
    path('<slug>/', detail_blog_view, name="detail"),#Sends user to post they created
]