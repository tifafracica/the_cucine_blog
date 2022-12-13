from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import ProfileForm, UserForm
from .models import Profile



# Create your views here.
class ProfileDetail(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'Posts/templates/Profiles/profile.html'
    

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'Posts/templates/Profiles/profile_form.html'
    def post(self, request, pk):
        Profile.objects.get_or_create(user=request.user)
        post_data = request.POST or None
        files_data = request.FILES or None
        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, files_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('Home'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)