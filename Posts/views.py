from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import CreatePostForm

# Create your views here.


def ShowIndex(request):
    
    return render(request, 'index.html')


def ShowHomePage(request):

    return render(request, 'home.html')


def ListPosts(request):

    return render(request, 'posts.html')

def ShowAboutPage(request):

    return render(request, 'about.html')

def CreateAPost(request):
    
    if request.method == 'POST':

        create_form = CreatePostForm(request.POST)

        if create_form.is_valid():

            clean_form = create_form.cleaned_data

            page_to_post = Post(title=clean_form['title'], content=clean_form['content'], post_img=clean_form['post_img'] )

            page_to_post.save()

            return render(request, 'posts.html')

    else:
        create_form = CreatePostForm()

    return render(request, 'create_post.html', {'create_form': create_form})

