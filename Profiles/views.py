from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile



# Create your views here.
def ShowProfilePage(request):
    return render(request, 'Posts/templates/Profiles/profile.html')
# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'Posts/templates/Profiles/profile_form.html'