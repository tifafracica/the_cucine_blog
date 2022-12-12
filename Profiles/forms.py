from django import forms
from django.contrib.auth.models import User

class CompleteProfileForm(forms.Form):

    description = forms.CharField(widget=forms.Textarea)
    web_page_link = forms.URLField()
    photo = forms.ImageField(label='your photo here')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
            ]