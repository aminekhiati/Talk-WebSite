from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length='50')
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name=forms.CharField(max_length=32, help_text='Last name')
    email=forms.EmailField(max_length=64, help_text='Enter a valid email address')
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)