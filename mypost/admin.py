from django.contrib import admin
from .models import *

admin.site.register([MyUser, Post, Category, CommentsModel, Chatting])
