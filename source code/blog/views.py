from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home Page'})

def about(request):
    return render(request, 'blog/about.html', {'title': 'Credits'})
