from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ShowIndex(request):
    
    return render(request, 'index.html')


def ShowHomePage(request):

    return render(request, 'home.html')


def ListPosts(request):

    return render(request, 'posts.html')