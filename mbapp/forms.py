from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'body']


class MessageUpdate(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'body']