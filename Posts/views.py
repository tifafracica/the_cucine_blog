from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm


# Create your views here.

def ShowIndex(request):   
    model = User
    return render(request, 'index.html')


def ShowHomePage(request):
    return render(request, 'home.html')


def ShowAboutPage(request):
    return render(request, 'about.html')


def findPage(request):
    if request.GET.get('title', False): 
        title = request.GET['title']
        posts = Post.objects.filter(title__icontains=title)
        return render(request, 'find_page.html', {'posts': posts})
    else:
        response = 'Post no found :('
    return render(request, 'find_page.html', {'response': response})

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'Posts/post_list.html'

class PostCreation(LoginRequiredMixin, CreateView):
    model = Post
    success_url = '/get_pages'
    fields = ['title', 'content', 'post_img']

class PostDetail(DetailView):
    model = Post
    template_name = 'Posts/post_detail.html'

class PostUpdate(UpdateView):
    model = Post
    success_url = '/get_pages'
    fields = ['title', 'content', 'post_img']

class PostDelete(DeleteView):
    model = Post
    success_url = '/get_pages'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'User/registration.html'

class AdminLoginView(LoginView):
    template_name = 'User/login.html'
    

class AdminLogoutView(LogoutView):
    template_name = 'User/logout.html'