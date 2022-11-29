from django import forms

class CompleteProfileForm(forms.Form):

    description = forms.CharField(widget=forms.Textarea)
    web_page_link = forms.URLField()
    photo = forms.ImageField(label='your photo here')