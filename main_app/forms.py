from django.forms import ModelForm
from .models import Message , Recipient

class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'ph_number']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['date', 'content', 'recipients']