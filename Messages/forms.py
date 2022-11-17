from django import forms

class CreateMessageForm(forms.Form):

    user = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    