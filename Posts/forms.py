from django import forms

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    post_img = forms.ImageField(label='Image',required=False)


