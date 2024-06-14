from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from account.models import Account

#Sign up/registration form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        #Checks password one and password two are identical
        fields = ("email", "username", "password1", "password2")


#Authentication
class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    #Checks email and password are correct
    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")


#Update account
class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username')

    #Checks the email isn't already used on the data base (no duplicates)
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except ObjectDoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)

    #Checks the username isn't already used on the data base (no duplicates)
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except ObjectDoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)