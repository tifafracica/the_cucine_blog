from django.shortcuts import render
from .models import Message
from .forms import CreateMessageForm
# Create your views here.

def ShowMessages(request):

    return render(request, 'messages.html')


def CreateAMessage(request):
    
    if request.method == 'POST':

        create_message_form = CreateMessageForm(request.POST)

        if create_message_form.is_valid():

            clean_form = create_message_form.cleaned_data

            page_to_post = Message(user=clean_form['user'], message=clean_form['message'])

            page_to_post.save()

            return render(request, 'messages.html')

    else:
        create_message_form = CreateMessageForm()

    return render(request, 'create_message.html', {'create_message_form': create_message_form})