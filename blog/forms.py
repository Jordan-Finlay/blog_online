from django import forms
from blog.models import BlogPost


#Allows user to create blog
class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']