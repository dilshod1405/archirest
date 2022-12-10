from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('avatar', 'role', 'about', 'login', 'password', 'username',)


class PostFormArchitect(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('file', 'category',)


class PostFormDesigner(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'category',)


class PostFormAllProfessions(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'file', 'category',)
