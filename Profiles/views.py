from django.shortcuts import render
from .models import Profile
from .forms import CompleteProfileForm

# Create your views here.
def ShowProfilePage(request):

    return render(request, 'profile.html')


def CompleteProfile(request):
    
    if request.method == 'POST':

        complete_profile_form = CompleteProfileForm(request.POST)

        if complete_profile_form.is_valid():

            clean_form = complete_profile_form.cleaned_data

            page_to_post = Profile(description=clean_form['description'], web_page_link=clean_form['web_page_link'],  photo=clean_form['photo'])

            page_to_post.save()

            return render(request, 'profile.html')

    else:
        complete_profile_form = CompleteProfileForm()

    return render(request, 'complite_profile.html', {'complete_profile_form': complete_profile_form})