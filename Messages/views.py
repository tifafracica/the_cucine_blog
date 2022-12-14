from .models import Message
from django.shortcuts import render, redirect
# Create your views here.
 
 
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("Login")
    context = {}
    return render(request, "Posts/templates/Messages/chatPage.html", context)