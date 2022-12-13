from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    web_page_link = forms.URLField()
    photo = forms.ImageField(label='Image',required=False)
    class Meta:
        model = Profile
        fields = ['description', 'web_page_link', 'photo']