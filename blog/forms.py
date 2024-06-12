from django import forms
from blog.models import BlogPost


#Allows user to create blog
class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']


#Allows users to edit their posts
class UpdateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']

    #Finds the title/body
    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']

        #Finds the image
        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']

        #If committed - Updates the post
        if commit:
            blog_post.save()
        return blog_post